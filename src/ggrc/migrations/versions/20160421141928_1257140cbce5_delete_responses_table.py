# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: goodson@google.com
# Maintained By: goodson@google.com

"""Delete responses table and any other references to responses

Create Date: 2016-04-21 14:19:28.527745
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '1257140cbce5'
down_revision = '5599d1769f25'


def upgrade():
    """Upgrade database schema and/or data, creating a new revision."""
    op.drop_constraint('meetings_ibfk_3', 'meetings', type_='foreignkey')
    op.drop_column('meetings', 'response_id')
    op.drop_table('responses')


def downgrade():
    """Downgrade database schema and/or data back to the previous revision."""
    op.create_table(
        'responses',
        sa.Column('title', sa.String(length=250), nullable=False),
        sa.Column('request_id', sa.Integer(), nullable=False),
        sa.Column(
            'response_type',
            sa.Enum(u'documentation', u'interview', u'population sample'),
            nullable=False),
        sa.Column('status', sa.String(length=250), nullable=False),
        sa.Column('population_worksheet_id', sa.Integer(), nullable=False),
        sa.Column('population_count', sa.Integer(), nullable=False),
        sa.Column('sample_worksheet_id', sa.Integer(), nullable=False),
        sa.Column('sample_count', sa.Integer(), nullable=False),
        sa.Column('sample_evidence_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['request_id'], ['requests.id']),
        sa.ForeignKeyConstraint(['population_worksheet_id'], ['documents.id']),
        sa.ForeignKeyConstraint(['sample_worksheet_id'], ['documents.id']),
        sa.ForeignKeyConstraint(['sample_evidence_id'], ['documents.id']),
        sa.Index('population_worksheet_document', 'population_worksheet_id'),
        sa.Index('sample_evidence_document', 'sample_evidence_id'),
        sa.Index('sample_worksheet_document', 'sample_worksheet_id')
    )

    op.add_column(
        'meetings', sa.Column('response_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'meetings_ibfk_3', 'meetings', 'responses', ['response_id'], ['id'])
