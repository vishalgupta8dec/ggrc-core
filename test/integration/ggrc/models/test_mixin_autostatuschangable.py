# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: urban@reciprocitylabs.com
# Maintained By: urban@reciprocitylabs.com

"""Integration test for AutoStatusChangable mixin"""

from ggrc import models

import integration.ggrc
from integration.ggrc import api_helper
from integration.ggrc.models import factories


class TestMixinAutoStatusChangable(integration.ggrc.TestCase):

  """Test case for AutoStatusChangable mixin"""

  # pylint: disable=invalid-name

  def setUp(self):
    integration.ggrc.TestCase.setUp(self)
    self.client.get("/login")
    self.api_helper = api_helper.Api()

  def test_open_to_in_progress_first_class_edit(self):
    """Test first class edit - it should move Assessment to Progress state"""
    assessment = self.create_assessment()

    self.assertEqual(assessment.status, models.Assessment.START_STATE)

    self.api_helper.modify_object(assessment, {
        "title": assessment.title + " modified, change #1"
    })
    assessment = self.refresh_object(assessment)
    self.assertEqual(assessment.status, models.Assessment.PROGRESS_STATE)

  def test_assessment_verifiers_full_cycle_first_class_edit(self):
    """Test Assessment with verifiers full flow

    Test moving from START_STATE to PROGRESS_STATE to FINAL_STATE and back to
    PROGRESS_STATE on edit.
    """
    assessment = self.create_assessment()

    self.assertEqual(assessment.status,
                     models.Assessment.START_STATE)

    assessment = self.refresh_object(assessment)

    self.api_helper.modify_object(assessment, {
        "title": assessment.title + " modified, change #1"
    })

    assessment = self.refresh_object(assessment)

    self.assertEqual(assessment.status,
                     models.Assessment.PROGRESS_STATE)

    assessment = self.change_status(assessment, assessment.DONE_STATE)

    self.assertEqual(assessment.title.endswith("modified, change #1"),
                     True)

    self.assertEqual(assessment.status,
                     models.Assessment.DONE_STATE)

    self.api_helper.modify_object(assessment, {
        "title": assessment.title + " modified, change #2"
    })
    assessment = self.refresh_object(assessment)
    self.assertEqual(assessment.title.endswith("modified, change #2"),
                     True)
    self.assertEqual(assessment.status,
                     models.Assessment.DONE_STATE)

    assessment = self.change_status(assessment,
                                    assessment.VERIFIED_STATE,
                                    assessment.FINAL_STATE)

    self.assertEqual(assessment.status, assessment.FINAL_STATE)
    self.assertEqual(assessment.verified, True)

    self.api_helper.modify_object(assessment, {
        "title": assessment.title + "modified, change #3"
    })
    assessment = self.refresh_object(assessment)
    self.assertEqual(assessment.title.endswith("modified, change #3"),
                     True)
    self.assertEqual(assessment.status,
                     models.Assessment.PROGRESS_STATE)

  @classmethod
  def create_assignees(cls, obj, persons):
    """Create assignees for object.
    Args:
      obj: Assignable object.
      persons: [("(string) email", "Assignee roles"), ...] A list of people
        and their roles
    Returns:
      [(person, object-person relationship,
        object-person relationship attributes), ...] A list of persons with
      their relationships and relationship attributes.
    """
    assignees = []
    for person, roles in persons:
      person = factories.PersonFactory(email=person)

      object_person_rel = factories.RelationshipFactory(
          source=obj,
          destination=person
      )

      object_person_rel_attrs = factories.RelationshipAttrFactory(
          relationship_id=object_person_rel.id,
          attr_name="AssigneeType",
          attr_value=roles
      )
      assignees += [(person, object_person_rel, object_person_rel_attrs)]
    return assignees

  def create_assessment(self, people=None):
    """Create default assessment with some default assignees in all roles.
    Args:
      people: List of tuples with email address and their assignee roles for
              Assessments.
    Returns:
      Assessment object.
    """
    assessment = factories.AssessmentFactory()

    if not people:
      people = [
          ("creator@example.com", "Creator"),
          ("assessor_1@example.com", "Assessor"),
          ("assessor_2@example.com", "Assessor"),
          ("verifier_1@example.com", "Verifier"),
          ("verifier_2@example.com", "Verifier"),
      ]

    self.create_assignees(assessment, people)

    creators = [assignee for assignee, roles in assessment.assignees
                if "Creator" in roles]
    assignees = [assignee for assignee, roles in assessment.assignees
                 if "Assessor" in roles]
    verifiers = [assignee for assignee, roles in assessment.assignees
                 if "Verifier" in roles]

    self.assertEqual(len(creators), 1)
    self.assertEqual(len(assignees), 2)
    self.assertEqual(len(verifiers), 2)
    return assessment

  @classmethod
  def refresh_object(cls, obj):
    """Returns a new instance of a model, fresh and warm from the database."""
    return obj.query.filter_by(id=obj.id).first()

  def change_status(self, obj, status,
                    expected_status=None, check_verified=False):
    """Change status of an object."""
    self.api_helper.modify_object(obj, {
        "status": status
    })
    obj = self.refresh_object(obj)
    if expected_status:
      self.assertEqual(obj.status, expected_status)
    else:
      self.assertEqual(obj.status, status)

    if check_verified:
      self.assertEqual(obj.verified, True)
    return obj
