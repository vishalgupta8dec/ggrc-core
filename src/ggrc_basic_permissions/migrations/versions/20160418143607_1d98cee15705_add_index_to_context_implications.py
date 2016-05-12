# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

"""
Add index to context_implications

Create Date: 2016-04-18 14:36:07.693364
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op

# revision identifiers, used by Alembic.
revision = '1d98cee15705'
down_revision = '3bf028a83e79'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  op.create_index('ix_context_implications_source_id', 'context_implications',
                  ['source_context_id'], unique=False)


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
  op.drop_index('ix_context_implications_source_id',
                table_name='context_implications')
