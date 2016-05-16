# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: ivan@reciprocitylabs.com
# Maintained By: ivan@reciprocitylabs.com

"""
  Assessment generator hooks

  We are applying assessment template properties and make
  new relationships and custom attributes
"""

from ggrc import db
from ggrc.login import get_current_user_id
from ggrc.automapper import AutomapperGenerator
from ggrc.models import all_models
from ggrc.models import Assessment
from ggrc.models import Person
from ggrc.models import Relationship
from ggrc.services.common import Resource


def init_hook():
  """ Initialize hooks"""
  # pylint: disable=unused-variable
  @Resource.model_posted_after_commit.connect_via(Assessment)
  def handle_assessment_post(sender, obj=None, src=None, service=None):
    # pylint: disable=unused-argument
    """Apply custom attribute definitions and map people roles
    when generating Assessmet with template"""

    map_assessment(obj, src.get("object"))
    map_assessment(obj, src.get("audit"))
    map_assessment(obj, src.get("program"))

    if not src.get("_generated"):
      return

    related = {
        "template": get_by_id(src.get("template")),
        "obj": get_by_id(src.get("object")),
        "audit": get_by_id(src.get("audit")),
    }
    relate_assignees(obj, related)
    relate_ca(obj, related)


def map_assessment(assessment, obj):
  """Creates a relationship between an assessment and an object. This also
  generates automappings. Fails silently if obj dict does not have id and type
  keys.

  Args:
    assessment (models.Assessment): The assessment model
    obj (dict): A dict with `id` and `type`.
  Returns:
    None
  """
  obj = obj or {}
  if 'id' not in obj or 'type' not in obj:
    return
  rel = Relationship(**{
      "source": assessment,
      "destination_id": obj["id"],
      "destination_type": obj["type"],
      "context": assessment.context,
  })
  AutomapperGenerator().generate_automappings(rel)
  db.session.add(rel)


def get_by_id(obj):
  """Get object instance by id"""
  if not obj:
    return

  model = get_model_query(obj["type"])
  return model.get(obj["id"])


def get_model_query(model_type):
  """Get model query"""
  model = getattr(all_models, model_type, None)
  return db.session.query(model)


def get_value(which, audit, obj, template=None):
  """Gets person value from string

      Args:
        which (string): type of people we are getting from template
        template (model instance): Template related to Assessment
        audit (model instance): Audit related to Assessment
        obj (model instance): Object related to Assessment
            (it can be any object in our app ie. Control,Issue, Facility...)
  """
  if not template:
    if which in ("assessors", "creator"):
      # don't use get_current_user because that returns a proxy
      return Person.query.get(get_current_user_id())
    return None

  types = {
      "Object Owners": [
          owner.person for owner in getattr(obj, 'object_owners', None)
      ],
      "Audit Lead": getattr(audit, 'contact', None),
      "Primary Contact": getattr(obj, 'contact', None),
      "Secondary Contact": getattr(obj, 'secondary_contact', None),
      "Primary Assessor": getattr(obj, 'principal_assessor', None),
      "Secondary Assessor": getattr(obj, 'secondary_assessor', None),
  }
  people = template.default_people.get(which)
  if not people:
    return None

  if isinstance(people, list):
    return [get_by_id({
        'type': 'Person',
        'id': person_id
    }) for person_id in people]
  return types.get(people)


def assign_people(assignees, assignee_role, assessment, relationships):
  """Create a list of people with roles

      Args:
        assignees (list of model instances): List of people
        assignee_role (string): It can be either Assessor or Verifier
        assessment (model instance): Assessment model
        relationships (list): List relationships between assignees and
                              assessment with merged AssigneeType's
  """
  assignees = assignees if isinstance(assignees, list) else [assignees]
  assignees = [assignee for assignee in assignees if assignee is not None]

  if not assignees and assignee_role != "Verifier":
    assignees.append(assessment.modified_by)

  for assignee in assignees:
    rel = (val for val in relationships if val["source"] == assignee)
    rel = next(rel, None)
    if rel:
      values = rel["attrs"]["AssigneeType"].split(",")
      values.append(assignee_role)
      rel["attrs"]["AssigneeType"] = ",".join(set(values))
    else:
      relationships.append(
          get_relationship_dict(assignee, assessment, assignee_role))


def get_relationship_dict(source, destination, role):
  """ Returns relationship object with Assignee Type"""
  return {
      "source": source,
      "destination": destination,
      "context": destination.context,
      "attrs": {
          "AssigneeType": role,
      },
  }


def relate_assignees(assessment, related):
  """Generates assignee list and relates them to Assessment objects

    Args:
        assessment (model instance): Assessment model
        related (dict): Dict containing model instances related to assessment
                        - obj
                        - audit
  """
  people_types = {
      "assessors": "Assessor",
      "verifiers": "Verifier",
      "creator": "Creator",
  }
  people_list = []

  for person_key, person_type in people_types.iteritems():
    assign_people(
        get_value(person_key, **related),
        person_type, assessment, people_list)

  for person in people_list:
    if person['source'] is not None and person['destination'] is not None:
      db.session.add(Relationship(**person))


def relate_ca(assessment, related):
  """Generates custom attribute list and relates it to Assessment objects

    Args:
        assessment (model instance): Assessment model
        related (dict): Dict containing model instances related to assessment
                        - template
                        - obj
                        - audit
  """
  if not related["template"]:
    return

  ca_query = all_models.CustomAttributeDefinition.eager_query()
  ca_definitions = ca_query.filter_by(
      definition_id=related["template"].id,
      definition_type="assessment_template",
  )

  for definition in ca_definitions:
    db.make_transient(definition)
    definition.id = None
    definition.definition_id = assessment.id
    definition.definition_type = assessment._inflector.table_singular
    db.session.add(definition)
