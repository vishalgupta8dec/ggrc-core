# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: peter@reciprocitylabs.com
# Maintained By: peter@reciprocitylabs.com

"""
Cascade delete workflow objects

Create Date: 2016-04-21 14:56:16.748579
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op


# revision identifiers, used by Alembic.
revision = '4fa163aa5dc4'
down_revision = '851b2f37a61'


def upgrade():
  """Add automatic cascade delete for workflow objects."""
  _update_constraints(ondelete="CASCADE")


def downgrade():
  """Remove automatic cascade delete for workflow objects."""
  _update_constraints(ondelete=None)


def _update_constraints(ondelete=None):
  """Update the ON DELETE rule for workflow objects' foreign key constrants.

  Args:
    ondelete: (str) An optional setting what should happen if a referenced
      record is deleted. Must be either CASCADE, DELETE or RESTRICT. If not
      provided, the behavior depends on the database defaults.
  """
  _update_fk_constraint(
      constraint_name="fk_workflow_people_workflow_id",
      src_table="workflow_people",
      src_columns=["workflow_id"],
      dest_table="workflows",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="fk_task_groups_workflow_id",
      src_table="task_groups",
      src_columns=["workflow_id"],
      dest_table="workflows",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="fk_task_group_tasks_task_group_id",
      src_table="task_group_tasks",
      src_columns=["task_group_id"],
      dest_table="task_groups",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="fk_task_group_objects_task_group_id",
      src_table="task_group_objects",
      src_columns=["task_group_id"],
      dest_table="task_groups",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycles_ibfk_3",
      src_table="cycles",
      src_columns=["workflow_id"],
      dest_table="workflows",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_groups_ibfk_3",
      src_table="cycle_task_groups",
      src_columns=["cycle_id"],
      dest_table="cycles",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_group_objects_cycle",
      src_table="cycle_task_group_objects",
      src_columns=["cycle_id"],
      dest_table="cycles",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_group_objects_ibfk_3",
      src_table="cycle_task_group_objects",
      src_columns=["cycle_task_group_id"],
      dest_table="cycle_task_groups",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_group_object_tasks_cycle",
      src_table="cycle_task_group_object_tasks",
      src_columns=["cycle_id"],
      dest_table="cycles",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_group_id",
      src_table="cycle_task_group_object_tasks",
      src_columns=["cycle_task_group_id"],
      dest_table="cycle_task_groups",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_entries_cycle",
      src_table="cycle_task_entries",
      src_columns=["cycle_id"],
      dest_table="cycles",
      dest_columns=["id"],
      ondelete=ondelete
  )

  _update_fk_constraint(
      constraint_name="cycle_task_entries_ibfk_2",
      src_table="cycle_task_entries",
      src_columns=["cycle_task_group_object_task_id"],
      dest_table="cycle_task_group_object_tasks",
      dest_columns=["id"],
      ondelete=ondelete
  )


def _update_fk_constraint(
    constraint_name, src_table, src_columns, dest_table, dest_columns,
    ondelete=None
):
  """Update the given foreign key constraint.

  Args:
    constraint_name: (str) Name of the foreign key constraint.
    src_table: (str) Name of the source (referencing) table.
    dest_table: (str) Name of the destination (referenced) table.
    src_columns: (list) String column names in the source table.
    dest_columns: (list) String column names in the destination table.
    ondelete: (str) An optional setting what should happen if a referenced
      record is deleted. Must be either CASCADE, DELETE or RESTRICT. If not
      provided, the behavior depends on the database defaults.
  """
  # Since this helper function is essentialy just a wrapper around Alembic's
  # method with a similar signature, silencing pylint is kind of justifiable.
  #
  # pylint: disable=too-many-arguments
  #
  op.drop_constraint(constraint_name, src_table, type_="foreignkey")
  op.create_foreign_key(
      constraint_name,
      src_table,
      dest_table,
      src_columns,
      dest_columns,
      ondelete=ondelete
  )
