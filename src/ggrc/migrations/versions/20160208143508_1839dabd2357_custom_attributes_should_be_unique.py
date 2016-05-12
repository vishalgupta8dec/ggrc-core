# Copyright (C) 2015 Reciprocity, Inc - All Rights Reserved
# Unauthorized use, copying, distribution, displaying, or public performance
# of this file, via any medium, is strictly prohibited. All information
# contained herein is proprietary and confidential and may not be shared
# with any third party without the express written consent of Reciprocity, Inc.
# Created By: rok@reciprocitylabs.com
# Maintained By: rok@reciprocitylabs.com

"""Custom attributes should be unique

Revision ID: 1839dabd2357
Revises: 4e989ef86619
Create Date: 2015-12-07 15:33:08.728216

"""

from alembic import op
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

from ggrc.app import app

# mandatory alembic variables
# pylint: disable=invalid-name

# revision identifiers, used by Alembic.
revision = '1839dabd2357'
down_revision = '4e989ef86619'


def upgrade():
  """Custom attributes have to be unique, so we find all of those that aren't,
  i.e. they have the same title and definition type and apply a consecutive
  index. Also deleting an attribute should cascade delete values."""
  conn = op.get_bind()

  # first, find potential duplicates
  find_duplicates_query = """
    select    ca.id, ca.title, ca.definition_type
    from      custom_attribute_definitions ca inner join
              custom_attribute_definitions ca2 on (
                ca.title = ca2.title and
                ca.definition_type = ca2.definition_type and
                ca.id != ca2.id)
    group by  ca.id
    order by  ca.title;
  """
  result = conn.execute(find_duplicates_query)
  duplicate_records = result.fetchall()
  attributes = [dict(zip(result.keys(), r)) for r in duplicate_records]

  # now, let's create a list of all the updates that we need to do
  previous_value = ""
  index = 0
  unique_count_query = ("SELECT COUNT(*) FROM custom_attribute_definitions "
                        "WHERE title = :title AND "
                        "definition_type = :definition_type")
  records_to_insert = {}
  for a in attributes:
    lowercase_title = a['title'].lower()  # mysql comparison is case insensitive (!) # noqa
    if previous_value != lowercase_title:
      previous_value = lowercase_title
      index = 0
    while True:
      index += 1
      new_title = "{} {}".format(a['title'], index)
      # we still need to check that the newly generated title does not collide
      # with an existing record in the db
      existing_records_alike = conn.execute(
          text(unique_count_query), title=new_title,
          definition_type=a['definition_type']
      ).first()[0]

      if existing_records_alike == 0 and \
         records_to_insert.get((new_title, a['definition_type'])) is None:
        break
      if index > 1000:
        # for more than 1000 duplicates we raise error and leave it to the user
        app.logger.error(
            'More than 1000 duplicates for title {} and definition_type {}'.
            format(a['title'], a['definition_type'])
        )
        raise StandardError
    records_to_insert[(new_title, a['definition_type'])] = (a['id'], new_title)

  # now, do the updates in a transaction
  update_record_query = ("UPDATE custom_attribute_definitions SET title = "
                         ":title WHERE id = :id")
  try:
    transaction = conn.begin()
    for _, v in records_to_insert.items():
      conn.execute(text(update_record_query), title=v[1], id=v[0])
    transaction.commit()
  except IntegrityError as error:
    app.logger.error(error)
    transaction.rollback()
    raise StandardError

  # finally, create unique constraints for future on now resolved duplicates
  op.create_unique_constraint(
      "uq_custom_attribute", "custom_attribute_definitions",
      ["title", "definition_type"])

  # make custom attributes cascade delete values
  sql1 = """
      alter table  custom_attribute_values
      drop         foreign key custom_attribute_values_ibfk_1"""
  sql2 = """
      alter table  custom_attribute_values
      add          constraint custom_attribute_values_ibfk_1
                   foreign key (custom_attribute_id)
      references   custom_attribute_definitions (id)
      on delete    cascade"""
  op.execute(sql1)
  op.execute(sql2)


def downgrade():
  op.drop_constraint("uq_custom_attribute", "custom_attribute_definitions",
                     type_="unique")

  sql1 = """
      alter table  custom_attribute_values
      drop         foreign key custom_attribute_values_ibfk_1"""
  sql2 = """
      alter table  custom_attribute_values
      add          constraint custom_attribute_values_ibfk_1
                   foreign key (custom_attribute_id)
      references   custom_attribute_definitions (id)"""
  op.execute(sql1)
  op.execute(sql2)
