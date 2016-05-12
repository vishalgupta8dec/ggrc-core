# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com


"""Make audit role implications to private programs mapped via responses

Revision ID: 3bb32fb65d47
Revises: 51e046bb002
Create Date: 2015-01-23 21:50:41.635827

"""

# revision identifiers, used by Alembic.
revision = '3bb32fb65d47'
down_revision = '51e046bb002'


def upgrade():
  """Migration is no longer applicable."""
  pass
  #   op.execute("""
  #     INSERT INTO context_implications (
  #       source_context_id, source_context_scope, context_id, context_scope
  #       )
  #     SELECT DISTINCT rs.context_id as source_context_id,
  #                     'Audit' AS source_context_scope,
  #                     p.context_id,
  #                     'Program' AS context_scope
  #     FROM relationships r
  #     INNER JOIN responses rs
  #       ON rs.id = r.source_id
  #       AND r.source_type IN ('Response', 'DocumentationResponse',
  #         'InterviewResponse')
  #     INNER JOIN programs p
  #       ON p.id = r.destination_id
  #       AND r.destination_type = 'Program'
  #     WHERE p.private = 1
  #     AND (SELECT count(*) from context_implications
  #          WHERE source_context_id = rs.context_id
  #          AND context_id = p.context_id) < 1
  #     """)

  #   op.execute("""
  #     INSERT INTO context_implications (
  #       source_context_id, source_context_scope, context_id, context_scope
  #       )
  #     SELECT DISTINCT sp.context_id as source_context_id,
  #                     'Program' AS source_context_scope,
  #                     p.context_id,
  #                     'Program' AS context_scope
  #     FROM relationships r
  #     INNER JOIN responses rs
  #       ON rs.id = r.source_id
  #       AND r.source_type IN ('Response', 'DocumentationResponse',
  #         'InterviewResponse')
  #     INNER JOIN requests rqs
  #       ON rqs.id = rs.request_id
  #     INNER JOIN audits a
  #       ON a.id = rqs.audit_id
  #     INNER JOIN programs sp
  #       ON sp.id = a.program_id
  #     INNER JOIN programs p
  #       ON p.id = r.destination_id
  #       AND r.destination_type = 'Program'
  #     WHERE p.private = 1
  #     AND (SELECT count(*) from context_implications
  #          WHERE source_context_id = sp.context_id
  #          AND context_id = p.context_id) < 1
  #     """)


def downgrade():
  """Migration is no longer applicable."""
  pass
  #   op.execute("""
  #     DELETE context_implications
  #     FROM context_implications ci
  #     INNER JOIN audits a ON a.context_id = ci.source_context_id
  #     INNER JOIN programs p ON p.context_id = ci.context_id
  #     WHERE a.program_id != p.id
  #     """)

  #   op.execute("""
  #     DELETE context_implications
  #     FROM context_implications ci
  #     INNER JOIN programs sp ON sp.context_id = ci.source_context_id
  #     INNER JOIN programs p ON p.context_id = ci.context_id
  #     """)
