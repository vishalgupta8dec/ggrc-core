# coding: utf-8
# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: miha@reciprocitylabs.com
# Maintained By: miha@reciprocitylabs.com

from integration.ggrc import TestCase

from ggrc import db
from ggrc.models.revision import Revision
from ggrc_workflows.notification.data_handler import get_cycle_task_dict
from integration.ggrc.models.factories import ContractFactory
from integration.ggrc.models.factories import EventFactory
from integration.ggrc.models.factories import RelationshipFactory
from integration.ggrc_workflows.models.factories import CycleTaskFactory


class TestDataHandler(TestCase):

  """ This class test basic functions in the data_handler module """
  def test_get_cycle_task_dict(self):
    contract = ContractFactory(title=u"Contract1")
    cycle_task = CycleTaskFactory(title=u"task1")
    relationship = RelationshipFactory(source=contract,
                                       destination=cycle_task)
    db.session.delete(relationship)
    db.session.commit()

    relationship_revision = Revision(obj=relationship,
                                     modified_by_id=None,
                                     action="deleted",
                                     content="{}")
    contract_revision = Revision(obj=contract,
                                 modified_by_id=None,
                                 action="deleted",
                                 content='{"display_name": "Contract1"}')
    revisions = [relationship_revision, contract_revision]
    EventFactory(
        modified_by_id=None,
        action="DELETE",
        resource_id=relationship.id,
        resource_type=relationship.type,
        context_id=None,
        revisions=revisions
    )
    task_dict = get_cycle_task_dict(cycle_task)
    self.assertEqual(task_dict["related_objects"][0],
                     u"Contract1 [removed from task]")

    # Test if we handle the title of the object being empty
    contract = ContractFactory(title=u"")
    cycle_task = CycleTaskFactory(title=u"task1")
    relationship = RelationshipFactory(source=contract,
                                       destination=cycle_task)

    task_dict = get_cycle_task_dict(cycle_task)
    self.assertEqual(task_dict["related_objects"][0],
                     u"Untitled object")
