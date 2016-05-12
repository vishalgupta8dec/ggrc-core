# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: samo@reciprocitylabs.com
# Maintained By: samo@reciprocitylabs.com

""" Unit tests for the Request object """

from sqlalchemy.orm import attributes

from ggrc import db
from ggrc.models import computed_property
from ggrc.models import mixins
from ggrc.models import mixins_assignable
from ggrc.models import object_document
from ggrc.models import object_person
from ggrc.models import relationship
from ggrc.models import Request

from unit.ggrc.models import test_mixins_base


class TestRequestMixins(test_mixins_base.TestMixinsBase):
  """ Tests inclusion of correct mixins and their attributes """

  def setUp(self):
    self.model = Request
    self.included_mixins = [
        mixins_assignable.Assignable,
        mixins.Base,
        mixins.CustomAttributable,
        mixins.Described,
        db.Model,
        object_document.Documentable,
        object_person.Personable,
        relationship.Relatable,
        mixins.Slugged,
        mixins.Titled,
    ]

    self.attributes_introduced = [
        ('assignees', property),                                        # Assignable    # noqa
        ('audit_id', attributes.InstrumentedAttribute),
        ('audit_object_id', attributes.InstrumentedAttribute),
        ('custom_attribute_values', attributes.InstrumentedAttribute),  # CustomAttrib. # noqa
        ('description', attributes.InstrumentedAttribute),              # Described     # noqa
        ('display_name', computed_property.computed_property),          # Base          # noqa
        ('end_date', attributes.InstrumentedAttribute),
        ('gdrive_upload_path', attributes.InstrumentedAttribute),
        ('notes', attributes.InstrumentedAttribute),
        ('object_documents', attributes.InstrumentedAttribute),         # Documentable  # noqa
        ('object_people', attributes.InstrumentedAttribute),            # Personable    # noqa
        ('related_sources', attributes.InstrumentedAttribute),          # Relatable     # noqa
        ('related_destinations', attributes.InstrumentedAttribute),     # Relatable     # noqa
        ('request_type', attributes.InstrumentedAttribute),
        ('start_date', attributes.InstrumentedAttribute),
        ('requestor', attributes.InstrumentedAttribute),
        ('requestor_id', attributes.InstrumentedAttribute),
        ('slug', attributes.InstrumentedAttribute),                     # Slugged       # noqa
        ('status', attributes.InstrumentedAttribute),
        ('test', attributes.InstrumentedAttribute),
        ('title', attributes.InstrumentedAttribute),                    # Titled        # noqa
    ]
