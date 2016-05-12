# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: samo@reciprocitylabs.com
# Maintained By: samo@reciprocitylabs.com

"""
Rename date columns in requests

Create Date: 2016-03-17 17:33:15.817255
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3715694bd315'
down_revision = '4db7ea2a47e9'


def upgrade():
  op.alter_column('requests', 'requested_on', new_column_name='start_date',
                  existing_type=sa.Date(), nullable=False)
  op.alter_column('requests', 'due_on', new_column_name='end_date',
                  existing_type=sa.Date(), nullable=False)


def downgrade():
  op.alter_column('requests', 'start_date', new_column_name='requested_on',
                  existing_type=sa.Date(), nullable=False)
  op.alter_column('requests', 'end_date', new_column_name='due_on',
                  existing_type=sa.Date(), nullable=False)
