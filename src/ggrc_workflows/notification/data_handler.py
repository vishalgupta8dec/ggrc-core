# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: miha@reciprocitylabs.com
# Maintained By: miha@reciprocitylabs.com

from copy import deepcopy
from datetime import date
from sqlalchemy import and_
from urlparse import urljoin

from ggrc import db
from ggrc import utils
from ggrc.models.revision import Revision
from ggrc.notifications import data_handlers
from ggrc.utils import merge_dicts, get_url_root
from ggrc_basic_permissions.models import Role, UserRole
from ggrc_workflows.models import Cycle
from ggrc_workflows.models import CycleTaskGroupObjectTask
from ggrc_workflows.models import Workflow


"""
exposed functions
    get_cycle_data,
    get_workflow_data,
    get_cycle_task_data,
"""


def get_cycle_created_task_data(notification):
  cycle_task = get_object(CycleTaskGroupObjectTask, notification.object_id)
  if not cycle_task:
    return {}

  cycle_task_group = cycle_task.cycle_task_group
  cycle = cycle_task_group.cycle

  force = cycle.workflow.notify_on_change

  task_assignee = data_handlers.get_person_dict(cycle_task.contact)
  task_group_assignee = data_handlers.get_person_dict(cycle_task_group.contact)
  workflow_owners = get_workflow_owners_dict(cycle.context_id)
  task = {
      cycle_task.id: get_cycle_task_dict(cycle_task)
  }

  result = {}

  assignee_data = {
      task_assignee['email']: {
          "user": task_assignee,
          "force_notifications": {
              notification.id: force
          },
          "cycle_started": {
              cycle.id: {
                  "my_tasks": deepcopy(task)
              }
          }
      }
  }
  tg_assignee_data = {
      task_group_assignee['email']: {
          "user": task_group_assignee,
          "force_notifications": {
              notification.id: force
          },
          "cycle_started": {
              cycle.id: {
                  "my_task_groups": {
                      cycle_task_group.id: deepcopy(task)
                  }
              }
          }
      }
  }
  for workflow_owner in workflow_owners.itervalues():
    wf_owner_data = {
        workflow_owner['email']: {
            "user": workflow_owner,
            "force_notifications": {
                notification.id: force
            },
            "cycle_started": {
                cycle.id: {
                    "cycle_tasks": deepcopy(task)
                }
            }
        }
    }
    result = merge_dicts(result, wf_owner_data)
  return merge_dicts(result, assignee_data, tg_assignee_data)


def get_cycle_task_due(notification):
  cycle_task = get_object(CycleTaskGroupObjectTask, notification.object_id)
  if not cycle_task:
    return {}

  notif_name = notification.notification_type.name
  due = "due_today" if notif_name == "cycle_task_due_today" else "due_in"
  force = cycle_task.cycle_task_group.cycle.workflow.notify_on_change
  return {
      cycle_task.contact.email: {
          "user": data_handlers.get_person_dict(cycle_task.contact),
          "force_notifications": {
              notification.id: force
          },
          due: {
              cycle_task.id: get_cycle_task_dict(cycle_task)
          }
      }
  }


def get_all_cycle_tasks_completed_data(notification, cycle):
  workflow_owners = get_workflow_owners_dict(cycle.context_id)
  force = cycle.workflow.notify_on_change
  result = {}
  for workflow_owner in workflow_owners.itervalues():
    wf_data = {
        workflow_owner['email']: {
            "user": workflow_owner,
            "force_notifications": {
                notification.id: force
            },
            "all_tasks_completed": {
                cycle.id: get_cycle_dict(cycle)
            }
        }
    }
    result = merge_dicts(result, wf_data)
  return result


def get_cycle_created_data(notification, cycle):
  if not cycle.is_current:
    return {}

  manual = notification.notification_type.name == "manual_cycle_created"
  force = cycle.workflow.notify_on_change
  result = {}

  for person in cycle.workflow.people:
    result[person.email] = {
        "user": data_handlers.get_person_dict(person),
        "force_notifications": {
            notification.id: force
        },
        "cycle_started": {
            cycle.id: get_cycle_dict(cycle, manual)
        }
    }
  return result


def get_cycle_data(notification):
  cycle = get_object(Cycle, notification.object_id)
  if not cycle:
    return {}

  notification_name = notification.notification_type.name
  if notification_name in ["manual_cycle_created", "cycle_created"]:
    return get_cycle_created_data(notification, cycle)
  elif notification_name == "all_cycle_tasks_completed":
    return get_all_cycle_tasks_completed_data(notification, cycle)

  return {}


def get_cycle_task_declined_data(notification):
  cycle_task = get_object(CycleTaskGroupObjectTask, notification.object_id)
  if not cycle_task:
    return {}

  force = cycle_task.cycle_task_group.cycle.workflow.notify_on_change
  return {
      cycle_task.contact.email: {
          "user": data_handlers.get_person_dict(cycle_task.contact),
          "force_notifications": {
              notification.id: force
          },
          "task_declined": {
              cycle_task.id: get_cycle_task_dict(cycle_task)
          }
      }
  }


def get_cycle_task_data(notification):

  cycle_task = get_object(CycleTaskGroupObjectTask, notification.object_id)
  if not cycle_task or not cycle_task.cycle_task_group.cycle.is_current:
    return {}

  notification_name = notification.notification_type.name
  if notification_name in ["manual_cycle_created", "cycle_created"]:
    return get_cycle_created_task_data(notification)
  elif notification_name == "cycle_task_declined":
    return get_cycle_task_declined_data(notification)
  elif notification_name in ["cycle_task_due_in",
                             "one_time_cycle_task_due_in",
                             "weekly_cycle_task_due_in",
                             "monthly_cycle_task_due_in",
                             "quarterly_cycle_task_due_in",
                             "annually_cycle_task_due_in",
                             "cycle_task_due_today"]:
    return get_cycle_task_due(notification)

  return {}


def get_workflow_starts_in_data(notification, workflow):
  if workflow.status != "Active":
    return {}
  if (not workflow.next_cycle_start_date or
     workflow.next_cycle_start_date < date.today()):
    return {}  # this can only be if the cycle has successfully started
  result = {}

  workflow_owners = get_workflow_owners_dict(workflow.context_id)
  force = workflow.notify_on_change

  for wf_person in workflow.workflow_people:
    result[wf_person.person.email] = {
        "user": data_handlers.get_person_dict(wf_person.person),
        "force_notifications": {
            notification.id: force
        },
        "cycle_starts_in": {
            workflow.id: {
                "workflow_owners": workflow_owners,
                "workflow_url": get_workflow_url(workflow),
                "start_date": workflow.next_cycle_start_date,
                "fuzzy_start_date": utils.get_fuzzy_date(
                    workflow.next_cycle_start_date),
                "custom_message": workflow.notify_custom_message,
                "title": workflow.title,
            }
        }
    }
  return result


def get_cycle_start_failed_data(notification, workflow):
  if workflow.status != "Active":
    return {}
  if (not workflow.next_cycle_start_date or
     workflow.next_cycle_start_date >= date.today()):
    return {}  # this can only be if the cycle has successfully started

  result = {}
  workflow_owners = get_workflow_owners_dict(workflow.context_id)
  force = workflow.notify_on_change

  for wf_owner in workflow_owners.itervalues():
    result[wf_owner["email"]] = {
        "user": wf_owner,
        "force_notifications": {
            notification.id: force
        },
        "cycle_start_failed": {
            workflow.id: {
                "workflow_owners": workflow_owners,
                "workflow_url": get_workflow_url(workflow),
                "start_date": workflow.next_cycle_start_date,
                "fuzzy_start_date": utils.get_fuzzy_date(
                    workflow.next_cycle_start_date),
                "custom_message": workflow.notify_custom_message,
                "title": workflow.title,
            }
        }
    }
  return result


def get_workflow_data(notification):
  workflow = get_object(Workflow, notification.object_id)
  if not workflow:
    return {}

  if workflow.frequency == "one_time":
    # one time workflows get cycles manually created and that triggers
    # the instant notification.
    return {}

  if "_workflow_starts_in" in notification.notification_type.name:
    return get_workflow_starts_in_data(notification, workflow)
  if "cycle_start_failed" == notification.notification_type.name:
    return get_cycle_start_failed_data(notification, workflow)

  return {}


def get_object(obj_class, obj_id):
  result = db.session.query(obj_class).filter(obj_class.id == obj_id)
  if result.count() == 1:
    return result.one()
  return None


def get_workflow_owners_dict(context_id):
  owners = db.session.query(UserRole).join(Role).filter(
      and_(UserRole.context_id == context_id,
           Role.name == "WorkflowOwner")).all()
  return {user_role.person.id: data_handlers.get_person_dict(user_role.person)
          for user_role in owners}


def _get_object_info_from_revision(revision, known_type):
  """ returns type and id of the searched object, if we have one part of
  the relationship known.
  """
  object_type = revision.destination_type \
      if revision.source_type == known_type \
      else revision.source_type
  object_id = revision.destination_id if \
      revision.source_type == known_type \
      else revision.source_id
  return object_type, object_id


def get_cycle_task_dict(cycle_task):

  object_titles = []
  # every object should have a title or at least a name like person object
  for related_object in cycle_task.related_objects:
    object_titles.append(getattr(related_object, "title", "") or
                         getattr(related_object, "name", "") or
                         u"Untitled object")
  # related objects might have been deleted or unmapped,
  # check the revision history
  deleted_relationships_sources = db.session.query(Revision).filter(
      Revision.resource_type == "Relationship",
      Revision.action == "deleted",
      Revision.source_type == "CycleTaskGroupObjectTask",
      Revision.source_id == cycle_task.id
  )
  deleted_relationships_destinations = db.session.query(Revision).filter(
      Revision.resource_type == "Relationship",
      Revision.action == "deleted",
      Revision.destination_type == "CycleTaskGroupObjectTask",
      Revision.destination_id == cycle_task.id
  )
  deleted_relationships = deleted_relationships_sources.union(
      deleted_relationships_destinations).all()
  for deleted_relationship in deleted_relationships:
    removed_object_type, removed_object_id = _get_object_info_from_revision(
        deleted_relationship, "CycleTaskGroupObjectTask")
    object_data = db.session.query(Revision).filter(
        Revision.resource_type == removed_object_type,
        Revision.resource_id == removed_object_id,
    ).one()

    object_titles.append(
        u"{} [removed from task]".format(object_data.content["display_name"])
    )

  return {
      "title": cycle_task.title,
      "related_objects": object_titles,
      "end_date": cycle_task.end_date.strftime("%m/%d/%Y"),
      "fuzzy_due_in": utils.get_fuzzy_date(cycle_task.end_date),
      "cycle_task_url": get_cycle_task_url(cycle_task),
  }


def get_cycle_dict(cycle, manual=False):
  workflow_owners = get_workflow_owners_dict(cycle.context_id)
  return {
      "manually": manual,
      "custom_message": cycle.workflow.notify_custom_message,
      "cycle_title": cycle.title,
      "workflow_owners": workflow_owners,
      "cycle_url": get_cycle_url(cycle),
  }


def get_workflow_url(workflow):
  url = "workflows/{}#current_widget".format(workflow.id)
  return urljoin(get_url_root(), url)


def get_cycle_task_url(cycle_task):
  url = ("/workflows/{workflow_id}#current_widget/cycle/{cycle_id}"
         "/cycle_task_group/{cycle_task_group_id}"
         "/cycle_task_group_object_task/{cycle_task_id}").format(
      workflow_id=cycle_task.cycle_task_group.cycle.workflow.id,
      cycle_id=cycle_task.cycle_task_group.cycle.id,
      cycle_task_group_id=cycle_task.cycle_task_group.id,
      cycle_task_id=cycle_task.id,
  )
  return urljoin(get_url_root(), url)


def get_cycle_url(cycle):
  url = "workflows/{workflow_id}#current_widget/cycle/{cycle_id}".format(
      workflow_id=cycle.workflow.id,
      cycle_id=cycle.id,
  )
  return urljoin(get_url_root(), url)
