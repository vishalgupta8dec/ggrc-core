# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: miha@reciprocitylabs.com
# Maintained By: miha@reciprocitylabs.com

"""Import all squashed migrations from 0.9.5-Zucchini-P1.

Revision ID: 262bbe790f4c
Revises: 297131e22e28
Create Date: 2016-01-19 14:35:08.577857


These migration were generated with the following procedure:

git checkout 0.9.5-Zucchini-P1
git checkout develop bin/db_reset
git reset HEAD bin/db_reset
all_modules=$GGRC_SETTINGS_MODULE
export GGRC_SETTINGS_MODULE="development"  # enable only the ggrc module
db_reset
mysqldump -uroot -proot ggrcdev > ggrcdev_ggrc.sql
export GGRC_SETTINGS_MODULE=all_modules
git checkout bin/db_reset
git checkout -


To test these migrations you can simply compare the migrations from two commits
develop - assuming the commit with this migration is rebased on top of the
  last develop branch.
squash - current commit

git checkout develop
db_reset && mysqldump -uroot -proot ggrcdev > dev.sql
git checkout squash
db_reset && mysqldump -uroot -proot ggrcdev > squ.sql


Note: Some of the squashed migrations can produce different database states
depending on if there was data in the db, when the migration was run. That is
why you should check you generated file and make the minor modifications to it,
so that the end result matches the migrations run before the squash, on an
empty database. If there are any differences in the databases, they should be
handled separately and not in this migration.
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

import os
from alembic import op

# revision identifiers, used by Alembic.
revision = '262bbe790f4c'
down_revision = None


def upgrade():
  """Import squashed migrations."""
  dirname = os.path.dirname(os.path.realpath(__file__))
  dump_file = os.path.join(dirname, "ggrcdev_ggrc.sql")
  dump = open(dump_file, "r")
  op.execute(dump.read())


def downgrade():
  pass
