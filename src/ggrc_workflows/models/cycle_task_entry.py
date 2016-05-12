# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: dan@reciprocitylabs.com
# Maintained By: peter@reciprocitylabs.com

"""A module containing the workflow CycleTaskEntry model."""


from sqlalchemy.ext.hybrid import hybrid_property

from ggrc import db
from ggrc.models.mixins import Base, Described
from ggrc.models.object_document import Documentable


class CycleTaskEntry(Described, Documentable, Base, db.Model):
  """Workflow CycleTaskEntry model."""

  __tablename__ = 'cycle_task_entries'

  _is_declining_review = db.Column(db.Boolean, nullable=True)

  cycle_id = db.Column(
      db.Integer,
      db.ForeignKey('cycles.id', ondelete="CASCADE"),
      nullable=False,
  )
  cycle_task_group_object_task_id = db.Column(
      db.Integer,
      db.ForeignKey('cycle_task_group_object_tasks.id', ondelete="CASCADE"),
      nullable=False,
  )
  cycle_task_group_object_task = db.relationship(
      'CycleTaskGroupObjectTask',
      foreign_keys='CycleTaskEntry.cycle_task_group_object_task_id',
      backref='cycle_task_entries',
  )

  _publish_attrs = [
      'cycle',
      'cycle_task_group_object_task',
      'is_declining_review'
  ]

  @hybrid_property
  def is_declining_review(self):
    return self._is_declining_review

  @is_declining_review.setter
  def is_declining_review(self, value):
    self._is_declining_review = bool(value)
