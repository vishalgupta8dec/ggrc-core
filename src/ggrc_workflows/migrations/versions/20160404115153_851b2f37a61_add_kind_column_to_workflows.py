# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: tomaz@reciprocitylabs.com
# Maintained By: tomaz@reciprocitylabs.com

"""Add column 'kind' to workflows

Revision ID: 851b2f37a61
Revises: 38af92d913dc
Create Date: 2016-04-04 11:51:53.349729

"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851b2f37a61'
down_revision = '38af92d913dc'


def upgrade():
  """The function adds a 'kind' column to the workflows table."""

  op.add_column('workflows',
                sa.Column('kind', sa.String(length=250), nullable=True))


def downgrade():
  """The function removes 'kind' column from workflows table."""

  op.drop_column('workflows', 'kind')
