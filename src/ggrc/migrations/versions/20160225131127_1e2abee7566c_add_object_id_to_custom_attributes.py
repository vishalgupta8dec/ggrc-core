# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: andraz@reciprocitylabs.com
# Maintained By: andraz@reciprocitylabs.com

"""Add object id to custom attributes

Revision ID: 1e2abee7566c
Revises: 1839dabd2357
Create Date: 2016-02-25 13:11:27.366833

"""
# Disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1e2abee7566c'
down_revision = '1839dabd2357'


def upgrade():
  op.add_column('custom_attribute_values',
                sa.Column('attribute_object_id', sa.Integer(), nullable=True))


def downgrade():
  op.drop_column('custom_attribute_values', 'attribute_object_id')
