# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

"""Base class for testing mixins on models"""

import unittest


class TestMixinsBase(unittest.TestCase):
  """Tests inclusion of correct mixins and their attributes"""

  def setUp(self):
    self.model = None
    self.included_mixins = []
    self.attributes_introduced = []

  def test_includes_correct_mixins(self):
    for mixin in self.included_mixins:
      self.assertTrue(
          issubclass(self.model, mixin),
          'Expected {} to inherit from {} but it does not'.format(
              self.model.__name__, mixin)
      )

  def test_correct_attrs_introduced(self):
    for attr_name, expected_type in self.attributes_introduced:
      actual_type = type(getattr(self.model, attr_name))
      self.assertEqual(
          expected_type,
          actual_type,
          'Expected attr "{}" to be of type {} but is actually {}'
          .format(attr_name, expected_type, actual_type)
      )
