# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: urban@reciprocitylabs.com
# Maintained By: urban@reciprocitylabs.com

"""Mixin for automatic status changes"""

import datetime

from sqlalchemy import inspect

from ggrc import db
from ggrc.models import relationship
from ggrc.models import object_document
from ggrc.services import common
from ggrc.services import signals
from ggrc.models import mixins_statusable


class AutoStatusChangable(object):
  """
  Mixin for automatic status changes

  Enables automatic transitioning of objects on any edit in cases where object
  has reached one of end states.
  """

  __lazy_init__ = True
  _tracked_attrs = set()

  FIRST_CLASS_EDIT = ({mixins_statusable.Statusable.START_STATE} |
                      mixins_statusable.Statusable.END_STATES)
  ASSIGNABLE_EDIT = mixins_statusable.Statusable.END_STATES

  @staticmethod
  def _date_has_changes(attr):
    """Detect if date attribute changed.

    Date fields are always interpreted as changed because incoming data is
    of type datetime.datetime, while database field has type datetime.date.

    This function normalises this and performs the correct check.

    Args:
      attr: (datetime.date|datetime.datetime) Attribute value
    Returns:
      A boolean representing if models date attribute really changed.
    """
    if not attr.history.added or not attr.history.deleted:
      return False
    added, deleted = attr.history.added[0], attr.history.deleted[0]
    if isinstance(added, datetime.datetime):
      added = added.date()
    return added != deleted

  @classmethod
  def _has_changes(cls, obj, attr):
    """Detects if object attribute has changes

    Args:
      obj: Object on which to perform attribute inspection.
      attr: Attribute to inspect
    Returns:
      A boolean representing if models attribute changed.
    """
    attr = getattr(inspect(obj).attrs, attr)
    if (isinstance(attr.value, datetime.date) or
       isinstance(attr.value, datetime.datetime)):
      return cls._date_has_changes(attr)
    return attr.history.has_changes()

  @classmethod
  def _get_object_from_relationship(cls, model, rel):
    """Get instance of an model object from relationship.

    Args:
      model: Class whose instance we want to retrieve from relationship.
      rel: Instance of relationship object.
    Returns:
      An instance of class model.
    """
    if rel.source.type == model.__name__:
      return rel.source
    return rel.destination

  @classmethod
  def init(cls, model):
    """Initialisation method to run after models have been initialised.

    Args:
      model: Class on which to run set_handlers method.
    Returns:
      Nothing.
    """
    cls.set_handlers(model)

  @staticmethod
  def adjust_status(model, obj):
    """Switches state on object to the PROGRESS_STATE

    Args:
      model: Class from which to read PROGRESS_STATE value.
      obj: object on which to perform status transition operation.
    Returns:
      Nothing.
    """
    obj.status = model.PROGRESS_STATE
    db.session.add(obj)

  @classmethod
  def handle_first_class_edit(cls, model, obj, rel=None):
    """Handles first class edit

    Performs check whether object received first class edit (ordinary edit
    that should transition object to PROGRESS_STATE from either: START_STATE
    or one of END_STATES.

    Args:
      model: Class from which to read FIRST_CLASS_EDIT property.
      obj: Object on which to perform operations.
      rel: Relationship object, needed here to maintain equal type signature
        with handle_person_edit.
    Returns:
      Nothing.
    """

    # pylint: disable=unused-argument,unused-variable

    if obj.status in model.FIRST_CLASS_EDIT:
      cls.adjust_status(model, obj)

  @classmethod
  def handle_person_edit(cls, model, obj, rel):
    """Handles person edit

    Args:
      model: Class from which to read ASSIGNABLE_EDIT property.
      obj: Object on which to perform operations.
      rel: Relationship whose attribute have to be inspected for changes.
    Returns:
      Nothing.
    """
    history = inspect(rel).attrs.relationship_attrs.history
    if (history.has_changes() and
       obj.status in model.ASSIGNABLE_EDIT):
      cls.adjust_status(model, obj)

  @classmethod
  def set_handlers(cls, model):
    """Sets up handlers of various events

    Args:
      model: Class on which handlers will be set up.
    Returns:
      Nothing.
    """
    @common.Resource.model_put.connect_via(model)
    def handle_object_put(sender, obj=None, src=None, service=None):
      """Handles object PUT operation

      Handles edit operation submitted to object.

      See blinker library documentation for other parameters (all necessary).

      Args:
        obj: Object on which we will perform manipulation.
      Returns:
        Nothing.
      """
      # pylint: disable=unused-argument,unused-variable,protected-access
      if (any(cls._has_changes(obj, attr) for attr in model._tracked_attrs) and
         model.FIRST_CLASS_EDIT):
        cls.handle_first_class_edit(model, obj)

    @signals.Signals.custom_attribute_changed.connect_via(model)
    def handle_custom_attribute_save(sender, obj=None, src=None, service=None):
      """Handles custom attribute save operation

      Handles INSERT or UPDATE(ish, because custom attributes are hackish)
      operations performed on custom attributes.

      See blinker library documentation for other parameters (all necessary).

      Args:
        obj: Object on which we will perform manipulation.
      """
      # pylint: disable=unused-argument,unused-variable

      cls.handle_first_class_edit(model, obj)

    @common.Resource.model_posted.connect_via(relationship.Relationship)
    @common.Resource.model_put.connect_via(relationship.Relationship)
    def handle_relationship_post(sender, obj=None, src=None, service=None):
      """Handle creation of relationships that can change object status.

      Adding or removing assigable persons (Assignees, Requesters, Creators,
      Verifiers, etc.) moves object back to PROGRESS_STATE.

      Adding evidence moves object back to to PROGRESS_STATE.

      See blinker library documentation for other parameters (all necessary).

      Args:
        obj: Object on which we will perform manipulation.
      Returns:
        Nothing
      """
      # pylint: disable=unused-argument,unused-variable

      endpoints = {obj.source.type, obj.destination.type}
      if model.__name__ in endpoints:
        target_object = cls._get_object_from_relationship(model, obj)

        handlers = {
            "Document": cls.handle_first_class_edit,
            "Person": cls.handle_person_edit
        }
        for k in handlers.keys():
          if k in endpoints:
            handlers[k](model, target_object, obj)

    @common.Resource.model_posted.connect_via(
        object_document.ObjectDocument)
    def handle_objectdocument_post(sender, obj=None, src=None, service=None):
      """Handles creation of URLs

      Adding URLs moves object back to PROGRESS_STATE.

      See blinker library documentation for other parameters (all necessary).

      Args:
        obj: Object on which we will perform manipulation.
      """
      # pylint: disable=unused-argument,unused-variable

      if obj.documentable.type == model.__name__:
        cls.handle_first_class_edit(model, obj.documentable)
