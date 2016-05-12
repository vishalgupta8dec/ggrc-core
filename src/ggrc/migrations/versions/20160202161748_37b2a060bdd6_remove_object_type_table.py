# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: miha@reciprocitylabs.com
# Maintained By: miha@reciprocitylabs.com


"""Remove object type table

Revision ID: 37b2a060bdd6
Revises: 6bed0575a0b
Create Date: 2016-02-02 16:17:48.928846

"""

# Disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=C0103

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '37b2a060bdd6'
down_revision = '6bed0575a0b'


def upgrade():
  """Remove object_type foreign key to notifications.

  Make sure the object_type in notifications is the same string field as in all
  other polymorphic tables and remove the now obsolete object_types tabele.
  """

  op.execute(
      "ALTER TABLE notifications "
      "ADD COLUMN object_type VARCHAR(250) NOT NULL "
      "AFTER object_id;"
  )

  op.execute(
      "UPDATE notifications AS n "
      "LEFT JOIN object_types AS o "
      "ON n.object_type_id = o.id "
      "SET n.object_type = o.name"
  )

  op.drop_constraint("notifications_ibfk_1", "notifications", "foreignkey")
  op.drop_column("notifications", "object_type_id")
  op.drop_table('object_types')


def downgrade():
  """Add object_type foreign key to notifications.

  Add the old object_types table and fill it with previous data, then replace
  object_type string field in notifications with object_type_id foreign key.
  """

  object_types_table = op.create_table(
      'object_types',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('name', sa.String(length=250), nullable=False),
      sa.Column('description', sa.String(length=250), nullable=True),
      sa.Column('created_at', sa.DateTime(), nullable=True),
      sa.Column('modified_by_id', sa.Integer(), nullable=True),
      sa.Column('updated_at', sa.DateTime(), nullable=True),
      sa.Column('context_id', sa.Integer(), nullable=True),
      sa.PrimaryKeyConstraint('id')
  )
  op.create_index('object_types_name', 'object_types', ['name'], unique=True)

  object_types_table = table(
      'object_types',
      column('id', sa.Integer),
      column('name', sa.String),
      column('description', sa.Text),
      column('created_at', sa.DateTime),
      column('modified_by_id', sa.Integer),
      column('updated_at', sa.DateTime),
      column('context_id', sa.Integer),
  )

  op.bulk_insert(
      object_types_table,
      [
          {"name": "Workflow", "description": ""},
          {"name": "TaskGroup", "description": ""},
          {"name": "TaskGroupTask", "description": ""},
          {"name": "TaskGroupObject", "description": ""},
          {"name": "Cycle", "description": ""},
          {"name": "CycleTaskGroup", "description": ""},
          {"name": "CycleTaskGroupObject", "description": ""},
          {"name": "CycleTaskGroupObjectTask", "description": ""},
      ]
  )
  op.add_column(
      "notifications",
      sa.Column("object_type_id", sa.Integer(), nullable=True)
  )

  op.execute(
      "UPDATE notifications AS n "
      "LEFT JOIN object_types AS o "
      "ON n.object_type = o.name "
      "SET n.object_type_id = o.id"
  )

  op.create_foreign_key("notifications_ibfk_1", "notifications",
                        "object_types", ["object_type_id"], ["id"])

  op.drop_column("notifications", "object_type")
