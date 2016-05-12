# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

"""Migrate Assessment to Assignable mixin

Revision ID: 6bed0575a0b
Revises: 1abb0a2e8ca0
Create Date: 2016-02-03 14:39:12.737518

"""

# Disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=C0103

from alembic import op

# revision identifiers, used by Alembic.
revision = '6bed0575a0b'
down_revision = '1abb0a2e8ca0'


def upgrade():
  op.execute("""
      INSERT IGNORE INTO relationships (
        modified_by_id, created_at, updated_at,
        source_id, source_type, destination_id, destination_type,
        context_id
      )
      SELECT
        oo.modified_by_id, NOW(), NOW(),
        oo.ownable_id, oo.ownable_type, oo.person_id, 'Person',
        oo.context_id
      FROM object_owners AS oo
      WHERE oo.ownable_type = 'Assessment'
  """)

  op.execute("""
      INSERT IGNORE INTO relationship_attrs (
        relationship_id, attr_name, attr_value
      )
      SELECT r.id, 'AssigneeType', 'Creator,Assessor'
      FROM relationships AS r
      JOIN object_owners AS oo
      ON r.destination_id = oo.person_id AND r.destination_type = 'Person'
      AND r.source_id = oo.ownable_id AND r.source_type = 'Assessment';
  """)

  op.execute("""UPDATE assessments SET status = 'Open'""")
  op.execute("""ALTER TABLE assessments
                CHANGE status status
                ENUM("Open","In Progress","Finished","Verified","Final")
                DEFAULT "Open"
                NOT NULL
  """)


def downgrade():
  pass
