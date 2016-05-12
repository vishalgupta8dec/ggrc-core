# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: andraz@reciprocitylabs.com
# Maintained By: andraz@reciprocitylabs.com

"""Module containing comment model and comment related mixins."""

from ggrc import db
from ggrc.models.mixins import Base
from ggrc.models.mixins import Described
from ggrc.models.object_document import Documentable
from ggrc.models.relationship import Relatable


class Commentable(object):
  """Mixin for commentable objects.

  This is a mixin for adding default options to objects on which people can
  comment.

  recipients is used for setting who gets notified (Verifer, Requester, ...).
  send_by_default should be used for setting the "send notification" flag in
    the comment modal.
  """

  recipients = db.Column(db.String, nullable=True)
  send_by_default = db.Column(db.Boolean)

  _publish_attrs = [
      "recipients",
      "send_by_default",
  ]
  _aliases = {
      "recipients": "Recipients",
      "send_by_default": "Send by default",
  }


class Comment(Relatable, Described, Documentable, Base, db.Model):
  """Basic comment model."""
  __tablename__ = "comments"

  assignee_type = db.Column(db.String)

  # REST properties
  _publish_attrs = [
      "assignee_type",
  ]

  _sanitize_html = [
      "description",
  ]
