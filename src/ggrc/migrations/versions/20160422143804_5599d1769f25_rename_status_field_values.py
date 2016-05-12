# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: urban@reciprocitylabs.com
# Maintained By: urban@reciprocitylabs.com

"""
Rename status field values

Create Date: 2016-04-22 14:38:04.330718
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name


from alembic import op

# revision identifiers, used by Alembic.
revision = "5599d1769f25"
down_revision = "33459bd8b70d"

TRANSLATION_TABLE = {
    "Open": "Not Started",
    "Finished": "Ready for Review",
    "Final": "Completed"
}

TABLES = ["assessments", "requests"]


def upgrade():
  for table in TABLES:
    op.execute("""
ALTER TABLE {table} CHANGE status status
ENUM("Open","In Progress","Finished", "Verified", "Final", "Not Started",
"Ready for Review", "Completed") NOT NULL;""".format(
        table=table))

    for old_value, new_value in TRANSLATION_TABLE.items():
      op.execute("""
UPDATE {table} SET status="{new_value}" WHERE status="{old_value}";""".format(
          table=table,
          new_value=new_value,
          old_value=old_value
      ))
    op.execute("""
ALTER TABLE {table} CHANGE status status
ENUM("Not Started", "In Progress", "Ready for Review", "Verified",
"Completed") NOT NULL;""".format(
        table=table))


def downgrade():
  for table in TABLES:
    op.execute("""
ALTER TABLE {table} CHANGE status status
ENUM("Not Started", "In Progress", "Ready for Review", "Verified",
"Completed", "Open", "Finished", "Final") NOT NULL;""".format(
        table=table))

    for old_value, new_value in TRANSLATION_TABLE.items():
      op.execute("""
UPDATE {table} SET status="{new_value}" WHERE status="{old_value}";""".format(
          table=table,
          new_value=old_value,
          old_value=new_value
      ))
    op.execute("""
ALTER TABLE {table} CHANGE status status
ENUM("Open","In Progress","Finished", "Verified", "Final") NOT NULL;""".format(
        table=table))
