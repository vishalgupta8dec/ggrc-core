# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: dan@reciprocitylabs.com
# Maintained By: peter@reciprocitylabs.com

"""A module containing the workflow WorkflowPerson model."""


from sqlalchemy.orm import backref

from ggrc import db
from ggrc.models.mixins import Mapping


class WorkflowPerson(Mapping, db.Model):
  """Workflow WorkflowPerson model."""

  __tablename__ = 'workflow_people'

  workflow_id = db.Column(
      db.Integer,
      db.ForeignKey('workflows.id', ondelete="CASCADE"),
      nullable=False,
  )
  person_id = db.Column(
      db.Integer, db.ForeignKey('people.id'), nullable=False)
  person = db.relationship(
      'Person',
      backref=backref('workflow_people', cascade='all, delete-orphan')
  )

  @staticmethod
  def _extra_table_args(klass):
    # pylint: disable=unused-argument
    return (
        db.UniqueConstraint('workflow_id', 'person_id'),
        db.Index('ix_workflow_id', 'workflow_id'),
        db.Index('ix_person_id', 'person_id'),
    )

  _publish_attrs = [
      'workflow',
      'person',
  ]
  _sanitize_html = []

  @classmethod
  def eager_query(cls):
    from sqlalchemy import orm

    query = super(WorkflowPerson, cls).eager_query()
    return query.options(
        orm.subqueryload('workflow'),
        orm.subqueryload('person'),
    )

  def _display_name(self):
    return self.person.display_name + '<->' + self.workflow.display_name
