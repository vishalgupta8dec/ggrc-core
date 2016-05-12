"""Add connected objects to revisions

Revision ID: 4e989ef86619
Revises: 37b2a060bdd6
Create Date: 2016-01-28 11:15:12.300329

"""

# pylint: disable=invalid-name

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e989ef86619'  # pylint: disable=invalid-name
down_revision = '37b2a060bdd6'  # pylint: disable=invalid-name


def upgrade():
  """ Add extra fields and indexes to revisions table """
  op.add_column('revisions', sa.Column('source_type', sa.String(length=250)))
  op.add_column('revisions', sa.Column('source_id', sa.Integer()))

  op.add_column('revisions',
                sa.Column('destination_type', sa.String(length=250)))
  op.add_column('revisions', sa.Column('destination_id', sa.Integer()))

  op.create_index('fk_revisions_resource', 'revisions',
                  ['resource_type', 'resource_id'], unique=False)
  op.create_index('fk_revisions_source', 'revisions',
                  ['source_type', 'source_id'], unique=False)
  op.create_index('fk_revisions_destination', 'revisions',
                  ['destination_type', 'destination_id'], unique=False)


def downgrade():
  """ Remove indexes and fields from revisions """
  op.drop_index('fk_revisions_resource', table_name='revisions')
  op.drop_index('fk_revisions_source', table_name='revisions')
  op.drop_index('fk_revisions_destination', table_name='revisions')

  op.drop_column('revisions', 'source_type')
  op.drop_column('revisions', 'source_id')
  op.drop_column('revisions', 'destination_type')
  op.drop_column('revisions', 'destination_id')
