# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

"""Admin dashboard page smoke tests"""
# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

import pytest    # pylint: disable=import-error
from lib import base
from lib import constants
from lib.page import dashboard


class TestAdminDashboardPage(base.Test):
  """Tests for the admin dashboard, a part of smoke tests, section 1"""
  _element = constants.element.AdminRolesWidget

  @pytest.mark.smoke_tests
  def test_roles_widget(self, selenium):
    """Confirms labels are present"""
    selenium.get(dashboard.AdminDashboard.URL)
    admin_roles_widget = dashboard\
        .AdminDashboard(selenium)\
        .select_roles()

    assert admin_roles_widget.role_editor.text == self._element.EDITOR
    assert admin_roles_widget.role_grc_admin.text == self._element.GRC_ADMIN
    assert admin_roles_widget.role_program_editor.text == \
        self._element.PROGRAM_EDITOR
    assert admin_roles_widget.role_program_owner.text == \
        self._element.PROGRAM_OWNER
    assert admin_roles_widget.role_program_reader.text == \
        self._element.PROGRAM_READER
    assert admin_roles_widget.role_reader.text == self._element.READER
    assert admin_roles_widget.role_workflow_member.text == \
        self._element.WORKFLOW_MEMEMBER
    assert admin_roles_widget.role_workflow_owner.text == \
        self._element.WORKFLOW_OWNER

    assert admin_roles_widget.scope_editor.text == self._element.SCOPE_SYSTEM
    assert admin_roles_widget.scope_grc_admin.text == self._element.SCOPE_ADMIN
    assert admin_roles_widget.scope_program_editor.text == \
        self._element.SCOPE_PRIVATE_PROGRAM
    assert admin_roles_widget.scope_program_owner.text == \
        self._element.SCOPE_PRIVATE_PROGRAM
    assert admin_roles_widget.scope_program_reader.text == \
        self._element.SCOPE_PRIVATE_PROGRAM
    assert admin_roles_widget.scope_reader.text == self._element.SCOPE_SYSTEM
    assert admin_roles_widget.scope_workflow_member.text == \
        self._element.SCOPE_WORKFLOW
    assert admin_roles_widget.scope_workflow_owner.text == \
        self._element.SCOPE_WORKFLOW
