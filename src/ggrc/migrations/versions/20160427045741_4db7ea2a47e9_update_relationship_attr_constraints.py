# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: miha@reciprocitylabs.com
# Maintained By: miha@reciprocitylabs.com

"""
update relationship attr constraints

Create Date: 2016-04-27 04:57:41.206892
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op


# revision identifiers, used by Alembic.
revision = '4db7ea2a47e9'
down_revision = '1257140cbce5'


def _update_constraint(ondelete=None):
  """Update relationship attrs foreign key constraint.

  Args:
    ondelete (str): The constraint on delete action that should be changed.
  """
  op.drop_constraint(
      "relationship_attrs_ibfk_1",
      "relationship_attrs",
      "foreignkey",
  )
  op.create_foreign_key(
      "relationship_attrs_ibfk_1",
      "relationship_attrs",
      "relationships",
      ["relationship_id"],
      ["id"],
      ondelete=ondelete,
  )


def upgrade():
  _update_constraint("CASCADE")


def downgrade():
  _update_constraint()
