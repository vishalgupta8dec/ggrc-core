# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: urban@reciprocitylabs.com
# Maintained By: urban@reciprocitylabs.com

from freezegun import freeze_time
from datetime import date

from ggrc import db
from ggrc_workflows.models import CycleTaskGroupObjectTask
from ggrc_workflows.models import Cycle
from ggrc_workflows.models import Workflow
from ggrc_workflows.models import CycleTaskGroup
from integration.ggrc_workflows.workflow_cycle_calculator import \
    base_workflow_test_case


class TestOneTimeWorkflow(base_workflow_test_case.BaseWorkflowTestCase):
  """One-time workflow tests

  With current implementation one-time cycles are started from the
  browser (workflow_page.js: Component "workflow-activate",
  function _activate), therefore you must always call generate_cycle
  before call activate.
  """

  def test_basic_one_time_workflow(self):
    """Basic one time workflow test.

    Testing if min max works.
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg_1",
            "task_group_tasks": [
                {
                    'title': 'task 1',
                    'start_date': date(2015, 6, 20),  # 6/18/2015 Thursday
                    'end_date': date(2015, 7, 3)  # 7/3/2015 Friday
                },
                {
                    'title': 'task 2',
                    'start_date': date(2015, 6, 18),  # 6/20/2015 Thursday
                    'end_date': date(2015, 8, 9)  # 8/9/2015 # Sunday
                }]
        }]
    }
    with freeze_time("2015-06-10 13:00:00"):  # 6/10/2015 Wednesday
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()
      self.assertEqual(active_wf.status, "Active")

      # one-time workflow shouldn't do date adjustment
      self.assertEqual(cycle.start_date, date(2015, 6, 18))
      self.assertEqual(cycle.end_date, date(2015, 8, 9))

  def test_future_start_month_after_end_month_next_year(self):
    """
      Testing that workflow is activated if it's
      * in the future
      * start_date.year < end_date.year
      * start_date.month > end_date.month
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg_1",
            "task_group_tasks": [
                {
                    'start_date': date(2014, 10, 1),
                    'end_date': date(2015, 5, 27)
                }]
        }]
    }
    with freeze_time("2014-09-25"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()

      self.assertEqual(active_wf.status, "Active")
      self.assertEqual(cycle.start_date, date(2014, 10, 1))
      self.assertEqual(cycle.end_date, date(2015, 5, 27))

  def test_future_start_month_before_end_month(self):
    """
      Testing that workflow is activated if it's
      * in the future
      * start_date.year < end_date.year
      * start_date.month < end_date.month
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg_1",
            "task_group_tasks": [
                {
                    'start_date': date(2014, 10, 1),
                    'end_date': date(2015, 11, 27)
                }]
        }]
    }
    with freeze_time("2014-09-25"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()

      self.assertEqual(active_wf.status, "Active")
      self.assertEqual(cycle.start_date, date(2014, 10, 1))
      self.assertEqual(cycle.end_date, date(2015, 11, 27))

  def test_past_start_month_after_end_month(self):
    """
      Testing that workflow is activated if it's
      * in the past
      * start_date.year < end_date.year
      * start_date.month > end_date.month
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg_1",
            "task_group_tasks": [
                {
                    'start_date': date(2014, 10, 1),
                    'end_date': date(2015, 5, 27)
                }]
        }]
    }
    with freeze_time("2015-06-01"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()

      cycle = cycle.__class__.query.get(cycle.id)
      self.assertEqual(active_wf.status, "Active")
      self.assertEqual(cycle.start_date, date(2014, 10, 1))
      self.assertEqual(cycle.end_date, date(2015, 5, 27))

  def test_past_start_month_before_end_month(self):
    """
      Testing that workflow is activated if it's
      * in the past
      * start_date.year < end_date.year
      * start_date.month < end_date.month
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg_1",
            "task_group_tasks": [
                {
                    'start_date': date(2014, 3, 1),
                    'end_date': date(2015, 5, 27)
                }]
        }]
    }

    with freeze_time("2015-06-01"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()

      cycle = cycle.__class__.query.get(cycle.id)
      self.assertEqual(active_wf.status, "Active")
      self.assertEqual(cycle.start_date, date(2014, 3, 1))
      self.assertEqual(cycle.end_date, date(2015, 5, 27))

  def test_adjust_end_date_when_tasks_get_deleted(self):
    """Test that deleting a longer running task updates cycle end date."""
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg 1",
            "task_group_tasks": [
                {
                    'title': 'one time task 1',
                    'start_date': date(2015, 7, 1),
                    'end_date': date(2015, 7, 8)
                },
                {
                    'title': 'one time task 2',
                    'start_date': date(2015, 7, 5),
                    'end_date': date(2015, 7, 11)
                }]
        }]
    }
    with freeze_time("2015-07-01"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, active_w_flow = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()
      self.assertEqual(active_wf.status, "Active")

      cycle = db.session.query(Cycle).filter(
          Cycle.workflow_id == w_flow.id).one()

      # First verify that the entire cycle window is covered
      self.assertEqual(cycle.start_date, date(2015, 7, 1))
      self.assertEqual(cycle.end_date, date(2015, 7, 11))

      cycle_task = db.session.query(CycleTaskGroupObjectTask).filter(
          CycleTaskGroupObjectTask.cycle_id == cycle.id,
          CycleTaskGroupObjectTask.title == "one time task 2"
      ).one()

      response = self.generator.api.delete(cycle_task)
      self.assert200(response)

      cycle = db.session.query(Cycle).filter(
          Cycle.workflow_id == w_flow.id).one()

      self.assertEqual(cycle.start_date, date(2015, 7, 1))
      self.assertEqual(cycle.end_date, date(2015, 7, 8))

  def test_adjust_end_date_when_cycle_tasks_get_added(self):
    """Test that adding a longer running cycle task updates cycle end date.
    This could happen with the modal for creating cycle tasks on the fly.
    """
    one_time_wf = {
        "title": "one time w_flow test",
        "description": "some test workflow",
        "task_groups": [{
            "title": "tg 1",
            "task_group_tasks": [
                {
                    'title': 'one time task 1',
                    'start_date': date(2015, 7, 1),
                    'end_date': date(2015, 7, 8)
                },
                {
                    'title': 'one time task 2',
                    'start_date': date(2015, 7, 5),
                    'end_date': date(2015, 7, 11)
                }]
        }]
    }
    with freeze_time("2015-07-01"):
      _, w_flow = self.generator.generate_workflow(one_time_wf)
      _, cycle = self.generator.generate_cycle(w_flow)
      _, awf = self.generator.activate_workflow(w_flow)

      active_wf = db.session.query(Workflow).filter(
          Workflow.id == w_flow.id).one()
      self.assertEqual(active_wf.status, "Active")

      cycle = db.session.query(Cycle).filter(
          Cycle.workflow_id == w_flow.id).one()
      cycle_task_group = db.session.query(CycleTaskGroup).filter(
          CycleTaskGroup.cycle_id == cycle.id).one()

      # First verify that the entire cycle window is covered
      self.assertEqual(cycle.start_date, date(2015, 7, 1))
      self.assertEqual(cycle.end_date, date(2015, 7, 11))

      # add a task that finishes after the current cycle
      cycle_task_json = {'cycle_task_group_object_task': {
          "title": "New added cycle task",
          "cycle": {"id": cycle.id, "type": "Cycle"},
          "status": "Assigned",
          "cycle_task_group": {
              "id": cycle_task_group.id,
              "type": "CycleTaskGroup"
          },
          "start_date": "07/1/2015",
          "end_date": "07/15/2015",
          "task_type": "text",
          "context": {
              "id": active_wf.context.id,
              "type": "Context"
          },
      }}
      self.generator.api.post(CycleTaskGroupObjectTask, cycle_task_json)
      cycle = db.session.query(Cycle).filter(
          Cycle.workflow_id == w_flow.id).one()

      self.assertEqual(cycle.start_date, date(2015, 7, 1))
      self.assertEqual(cycle.end_date, date(2015, 7, 15))

      # add a task that finishes before the first task in the cycle
      cycle_task_json = {'cycle_task_group_object_task': {
          "title": "New added cycle task that is due soon",
          "cycle": {"id": cycle.id, "type": "Cycle"},
          "status": "Assigned",
          "cycle_task_group": {
              "id": cycle_task_group.id,
              "type": "CycleTaskGroup"
          },
          "start_date": "07/1/2015",
          "end_date": "07/2/2015",
          "task_type": "text",
          "context": {
              "id": active_wf.context.id,
              "type": "Context"
          },
      }}
      self.generator.api.post(CycleTaskGroupObjectTask, cycle_task_json)

      cycle_task_group = db.session.query(CycleTaskGroup).filter(
          CycleTaskGroup.cycle_id == cycle.id).one()
      self.assertEqual(cycle_task_group.next_due_date, date(2015, 7, 2))
