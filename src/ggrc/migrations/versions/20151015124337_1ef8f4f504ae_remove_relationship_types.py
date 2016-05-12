# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: andraz@reciprocitylabs.com
# Maintained By: andraz@reciprocitylabs.com

"""Remove relationship_types

Revision ID: 1ef8f4f504ae
Revises: 262bbe790f4c
Create Date: 2015-10-15 12:43:37.846021

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1ef8f4f504ae'
down_revision = '262bbe790f4c'


def upgrade():
  try:
    op.drop_column('relationships', 'relationship_type_id')
  except sa.exc.OperationalError as operr:
    # Ignores error in case relationship_type_id no longer exists
    error_code, _ = operr.orig.args  # error_code, message
    if error_code != 1091:
      raise operr

  try:
    op.drop_table('relationship_types')
  except sa.exc.OperationalError as operr:
    # Ignores error in case relationship_types table no longer exists
    error_code, _ = operr.orig.args  # error_code, message
    if error_code != 1051:
      raise operr


def downgrade():
  op.create_table(
      'relationship_types',
      sa.Column('id', sa.INTEGER),
      sa.Column('modified_by_id', sa.INTEGER),
      sa.Column('created_at', sa.DATETIME),
      sa.Column('updated_at', sa.DATETIME),
      sa.Column('description', sa.TEXT),
      sa.Column('relationship_type', sa.VARCHAR(length=250)),
      sa.Column('forward_phrase', sa.VARCHAR(length=250)),
      sa.Column('backward_phrase', sa.VARCHAR(length=250)),
      sa.Column('symmetric', sa.BOOLEAN, nullable=False),
      sa.Column('context_id', sa.INTEGER),
      sa.ForeignKeyConstraint(['context_id'], [u'contexts.id'],
                              name=u'fk_relationship_types_contexts'),
      sa.PrimaryKeyConstraint('id')
  )
  op.add_column(
      'relationships',
      sa.Column('relationship_type_id', sa.String(length=250), nullable=True)
  )
