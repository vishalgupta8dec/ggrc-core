# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: peter@reciprocitylabs.com
# Maintained By: peter@reciprocitylabs.com

"""A module with tests for the GGRC Workflow package.

It contains unit tests for the package's top level utility functions.
"""

import unittest

from datetime import datetime, timedelta

from mock import MagicMock, patch

from freezegun import freeze_time
from ggrc_workflows import adjust_next_cycle_start_date


class AdjustNextCycleStartDateTestCase(unittest.TestCase):
  """Tests for the adjust_next_cycle_start_date() function."""

  def setUp(self):
    self.workflow = MagicMock(name="workflow")
    self.wf_calculator = MagicMock(name="workflow_calculator")

    self.wf_calculator.time_delta = timedelta(weeks=1)
    self.wf_calculator.non_adjusted_next_cycle_start_date = \
        lambda base_date: base_date + self.wf_calculator.time_delta

  # pylint: disable=invalid-name
  @patch("ggrc_workflows.get_cycles")
  def test_handling_datetime_objects(self, get_cycles):
    """The method should know how to handle datetime.datetime objects.

    The reason is that workflow cycle calculator does not always return
    datetime.date objects if passed a datetime.datetime argument.
    """
    cycle_task = MagicMock(name="cycle_task")
    cycle_task.start_date = datetime(2016, 02, 21)
    get_cycles.return_value = [cycle_task]

    self.workflow.recurrences = True
    self.workflow.non_adjusted_next_cycle_start_date = None

    self.wf_calculator.tasks = [MagicMock(name="task_1")]
    self.wf_calculator.relative_day_to_date.side_effect = [
        datetime(2016, 3, 15),
        datetime(2016, 6, 6),
    ]

    try:
      with freeze_time("2016-05-10 14:26:18"):
        adjust_next_cycle_start_date(self.wf_calculator, self.workflow)
    except TypeError:
      self.fail("The method should handle datetime.datetime without errors.")
