# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

"""Locators for all the elements"""
# pylint: disable=too-few-public-methods

from selenium.webdriver.common.by import By   # pylint: disable=import-error
from lib.constants import objects
from lib.constants import attribute


class Login(object):
  """All locators for the login page"""

  BUTTON_LOGIN = (By.CSS_SELECTOR, "a.btn.btn-large.btn-info")


class PageHeader(object):
  """All locators for the dashboard header (has the same name as the elemnt"""

  TOGGLE_LHN = (By.CSS_SELECTOR, ".lhn-trigger")
  BUTTON_DASHBOARD = (By.CSS_SELECTOR, '.header-content .to-my-work['
                                       'href="/dashboard"]')
  BUTTON_SEARCH = (By.CSS_SELECTOR, '.header-content ['
                                    'data-toggle="unified-search"]')
  BUTTON_MY_TASKS = (By.CSS_SELECTOR, '.header-content ['
                                      'href="/dashboard#task_widget"]')
  BUTTON_ALL_OBJECTS = (By.CSS_SELECTOR, '.header-content ['
                                         'href="/objectBrowser"]')
  TOGGLE_USER_DROPDOWN = (
      By.CSS_SELECTOR, '.header-content .dropdown-toggle')
  BUTTON_HELP = (By.CSS_SELECTOR, '.header-content [id="#page-help"]')

  # dropdown toggle
  BUTTON_ADMIN_DASHBOARD = (
      By.CSS_SELECTOR, '.dropdown-menu [href="/admin#people_list_widget"]')
  BUTTON_MY_WORK = (By.CSS_SELECTOR, '.dropdown-menu [href="/dashboard"]')
  BUTTON_DATA_IMPORT = (By.CSS_SELECTOR, '.dropdown-menu [href="/import"]')
  BUTTON_DATA_EXPORT = (By.CSS_SELECTOR, '.dropdown-menu [href="/export"]')
  BUTTON_LOGOUT = (By.CSS_SELECTOR, '.dropdown-menu [href="/logout"]')
  NOTIFICATIONS = (By.CSS_SELECTOR, '.menu .user-dropdown .notify-wrap')
  CHECKBOX_DAILY_DIGEST = (By.CSS_SELECTOR, '.menu .user-dropdown input')
  CHECKBOX_DISABLED = (By.CSS_SELECTOR, '.menu .user-dropdown input.disabled')


class Dashboard(object):
  """Locators for the dashbord page"""

  BUTTON_START_NEW_PROGRAM = (
      By.CSS_SELECTOR, '.get-started__list [data-object-singular="Program"]')
  BUTTON_START_NEW_AUDIT = (
      By.CSS_SELECTOR, '.get-started__list [data-object-singular="Audit"]')
  BUTTON_START_NEW_WORKFLOW = (
      By.CSS_SELECTOR, '.get-started__list [data-object-singular="Workflow"]')
  BUTTON_CREATE_NEW_OBJECT = (
      By.CSS_SELECTOR, '.get-started__list [href="#"]')
  BUTTON_ALL_OBJECTS = (By.CSS_SELECTOR, '.get-started__list '
                                         '[href="/objectBrowser"]')


class LhnMenu(object):
  """Locators for the menu in header"""
  class _Locator(object):
    @staticmethod
    def get_accordion_button(label):
      return (By.CSS_SELECTOR, '[data-model-name="{}"]>a'.format(label))

    @staticmethod
    def get_create_new_button(label):
      return (
          By.CSS_SELECTOR,
          '[data-model-name="{}"] [data-test-id="button_lhn_create_new_program'
          '_522c563f"]'.format(label))

    @staticmethod
    def get_accordion_count(label):
      return (By.CSS_SELECTOR, '[data-model-name="{}"] .item-count'.format(
          label))

    @staticmethod
    def get_accordion_members(object_name):
      return (
          By.CSS_SELECTOR,
          '[data-model-name="{}"]>.content>.sub-level>li'.format(object_name))

    @staticmethod
    def get_spinny(object_name):
      return (By.CSS_SELECTOR, '[data-model-name="{}"] .spinny'.format(
          object_name))

  class __metaclass__(type):
    def __init__(self, *args):
      for object_singular, object_plural in zip(objects.ALL_SINGULAR,
                                                objects.ALL_PLURAL):
        capitalized_name = object_singular.title()

        # handle underscore in object names
        if "_" in capitalized_name:
          capitalized_name = capitalized_name.title().replace("_", "")

        # set lhn items
        setattr(self, attribute.TOGGLE + object_plural,
                self._Locator.get_accordion_button(capitalized_name))
        setattr(self, attribute.BUTTON_CREATE_NEW + object_plural,
                self._Locator.get_create_new_button(capitalized_name))
        setattr(self, attribute.COUNT + object_plural,
                self._Locator.get_accordion_count(capitalized_name))
        setattr(self, attribute.SPINNY + object_plural,
                self._Locator.get_spinny(capitalized_name))
        setattr(self, attribute.ACCORDION_MEMBERS + object_plural,
                self._Locator.get_accordion_members(capitalized_name))

  LHN_MENU = (By.ID, "lhn")
  MODAL = (By.CSS_SELECTOR, '[id="ajax-lhn_modal-javascript:--"]')
  EXTENDED_INFO = (By.CSS_SELECTOR, '.extended-info.in')

  FILTER = (By.CSS_SELECTOR, '.lhs-search')
  FILTER_TEXT_BOX = (By.CSS_SELECTOR, '.lhs-search>.widgetsearch')
  FILTER_SUBMIT_BUTTON = (
      By.CSS_SELECTOR, '.lhs-search>.widgetsearch-submit')
  FILTER_CLEAR_BUTTON = (
      By.CSS_SELECTOR, '.lhs-search [data-title="Clear filters"]')

  LHS_ITEM = (By.CSS_SELECTOR, '[test-data-id="lhs-item_3ad27b8b"]')
  ALL_OBJECTS = (By.CSS_SELECTOR, '[data-test-id="all_objects_e0345ec4"]')
  MY_OBJECTS = (By.CSS_SELECTOR, '[data-test-id="my_objects_6fa95ae1"]')
  PIN = (By.CSS_SELECTOR, '.lhn-pin')

  # lhn items
  DIRECTIVES = (By.CSS_SELECTOR, '[data-test-id="directives_66116337"]')
  TOGGLE_CONTROLS_OR_OBJECTIVES = (
      By.CSS_SELECTOR, '[data-test-id="controls/objectives_66116337"]')
  TOGGLE_PEOPLE_OR_GROUPS = (
      By.CSS_SELECTOR, '[data-test-id="people/groups_66116337"]')
  TOGGLE_ASSETS_OR_BUSINESS = (
      By.CSS_SELECTOR, '[data-test-id="assets/business_66116337"]')
  TOGGLE_RISK_OR_THREATS = (
      By.CSS_SELECTOR, '[data-test-id="risk/threats_66116337"]')

  # workflows labels
  BUTTON_WORKFLOWS_ACTIVE = (
      By.CSS_SELECTOR, '[data-for="Workflow"]>[data-value="Active"]')
  BUTTON_WORKFLOWS_DRAFT = (
      By.CSS_SELECTOR, '[data-for="Workflow"]>[data-value="Draft"]')
  BUTTON_WORKFLOWS_INACTIVE = (
      By.CSS_SELECTOR, '[data-for="Workflow"]>[data-value="Inactive"]')


class ExtendedInfo(object):
  """Locators for the extended info tooltip in LHN after hovering over a
  member object"""

  BUTTON_MAP_TO = (
      By.CSS_SELECTOR, '[data-test-id="extended_info_button_map"]')
  ALREADY_MAPPED = (
      By.CSS_SELECTOR, '[data-test-id="extended_info_object_already_mapped"]')
  TITLE = (By.CSS_SELECTOR, '#extended-info .main-title')


class BaseModalCreateNew(object):
  """Locators shared with create new object modals"""
  # labels
  MODAL_TITLE = (By.CSS_SELECTOR, '[id="ajax-modal-javascript:--"]>div>h2')
  TITLE = (By.CSS_SELECTOR, '.modal-body form>div:nth-child(2) .span6>label')

  # user input elements
  UI_TITLE = (
      By.CSS_SELECTOR,
      '.modal-body form>div:nth-child(2) .span6>input')


class ModalCreateNewProgram(BaseModalCreateNew):
  """Locators for the program modal visible when creating a new modal from
  LHN"""
  UI_TITLE = (By.CSS_SELECTOR,
              '[data-test-id="new_program_field_title_a63ed79d"]')
  UI_DESCRIPTION = (By.CSS_SELECTOR,
                    '[data-test-id="new_program_field_description_1fb8bc06"]'
                    '>iframe.wysihtml5-sandbox')
  UI_NOTES = (By.CSS_SELECTOR,
              '[data-test-id="new_program_field_notes_75b8bc05"]'
              '>iframe.wysihtml5-sandbox')
  UI_CODE = (By.CSS_SELECTOR,
             '[data-test-id="new_program_field_code_334276e2"]')
  UI_STATE = (By.CSS_SELECTOR,
              '[data-test-id="new_program_dropdown_state_036a1fa6"]')
  BUTTON_HIDE_OPTIONAL_FIELDS = (By.ID, "formHide")
  BUTTON_SHOW_ALL_OPTIONAL_FIELDS = (By.ID, "formHide")
  UI_PRIMARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id='
                                         '"new_program_field_primary_contact_'
                                         '86160053"]')
  DROPDOWN_CONTACT = (By.CSS_SELECTOR, '.ui-menu-item')
  UI_SECONDARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id='
                                           '"new_program_field_secondary_'
                                           'contact_'
                                           '86160053"]')

  UI_PROGRAM_URL = (By.CSS_SELECTOR, '[data-test-id='
                                     '"new_program_field_program_url_'
                                     '86160053"]')
  UI_REFERENCE_URL = (By.CSS_SELECTOR, '[data-test-id='
                                       '"new_program_field_reference_url_'
                                       '86160053"]')
  UI_EFFECTIVE_DATE = (By.CSS_SELECTOR, '[data-test-id='
                                        '"new_program_field_effective_date_'
                                        'f2783a28"]')
  UI_STOP_DATE = (By.CSS_SELECTOR, '[data-test-id='
                                   '"new_program_field_stop_date_f2783a28"]')
  DATE_PICKER = (By.CSS_SELECTOR, '.ui-datepicker-calendar ['
                                  'data-handler="selectDay"]')
  TITLE = (By.CSS_SELECTOR, '[data-test-id="label_title_2c925d94"]')
  DESCRIPTION = (By.CSS_SELECTOR,
                 '[data-test-id="label_description_2c925d94"]')

  PRIVACY = (By.CSS_SELECTOR, '[data-test-id="label_privacy_2c925d94"]')
  PROGRAM_URL = (By.CSS_SELECTOR,
                 '[data-test-id="label_program_url_2c925d94"]')


class ModalCreateNewOrgGroup(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewRisk(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""
  UI_DESCRIPTION = (
      By.CSS_SELECTOR, '.modal-body form>div:nth-child(3) iframe')


class ModalCreateRequest(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewDataAsset(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewProcess(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewProject(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewSystem(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewProduct(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""


class ModalCreateNewControl(BaseModalCreateNew):
  """Locators for the control modal visible when creating a new modal from
  LHN"""
  class _Locator(object):
    @staticmethod
    def get_asessor_row(first_id, second_id):
      return (
          By.CSS_SELECTOR,
          '.modal-body div>form>div>div:nth-child({})>div:nth-child({}) '
          'label'.format(first_id, second_id))

    @staticmethod
    def get_dropdown_item(first_id, second_id):
      return (
          By.CSS_SELECTOR,
          '.modal-body div>form>div>div:nth-child({})>div:nth-child({}) '
          'select'.format(first_id, second_id))

  # labels
  DESCRIPTION = (
      By.CSS_SELECTOR, '.modal-body form>div:nth-child(3) .span6>label')
  TEST_PLAN = (By.CSS_SELECTOR, '[data-id="test_plan_hidden"] label')
  NOTES = (By.CSS_SELECTOR, '[data-id="note_hidden"] label')
  CODE = (By.CSS_SELECTOR, '[data-id="code_hidden"] label')
  KIND_OR_NATURE = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(6) div:nth-child(2) div:nth-child(1) label')
  FRAUD_RELATED = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(6) div:nth-child(2) div:nth-child(2) label')
  EFFECTIVE_DATE = _Locator.get_asessor_row(3, 1)
  FREQUENCY = _Locator.get_asessor_row(4, 1)
  ASSERTIONS = _Locator.get_asessor_row(4, 2)
  PRINCIPAL_ASSESSOR = _Locator.get_asessor_row(5, 1)
  SECONDARY_ASSESSOR = _Locator.get_asessor_row(5, 2)

  OWNER = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(3) div:nth-child(2) '
      'label')
  PRIMARY_CONTACT = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(4) div:nth-child(2)>'
      'div:nth-child(1)>div>label')
  SECONDARY_CONTACT = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(4) div:nth-child(2)>'
      'div:nth-child(2)>div>label')
  CONTROL_URL = (
      By.CSS_SELECTOR,
      '.modal-body form>div:nth-child(5) div:nth-child(2)>div:nth-child(1)>div'
      '>label')
  REFERENCE_URL = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(5) div:nth-child(2)>'
      'div:nth-child(2)>div>label')
  SIGNIFICANCE = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(6) div:nth-child(2) div:nth-child(3) label')
  TYPE_OR_MEANS = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(6) div:nth-child(2) div:nth-child(4) label')
  STOP_DATE = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(6) div:nth-child(3) div:nth-child(2) label')
  CATEGORIES = (
      By.CSS_SELECTOR,
      '.modal-body div>form>div>div:nth-child(4)>div:nth-child(3) label')
  STATE = (
      By.CSS_SELECTOR,
      '.modal-body div>form>div>div:nth-child(5)>div:nth-child(3) label')

  # user input elements
  UI_DESCRIPTION = (
      By.CSS_SELECTOR, '.modal-body form>div:nth-child(3) iframe')
  UI_TEST_PLAN = (By.CSS_SELECTOR, '[data-id="test_plan_hidden"] iframe')
  UI_NOTES = (By.CSS_SELECTOR, '[data-id="note_hidden"] iframe')
  UI_CODE = (By.CSS_SELECTOR, '[data-id="code_hidden"] input')
  UI_PRIMARY_CONTACT = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(4) div:nth-child(2)>'
      'div:nth-child(1)>div>input')
  UI_SECONDARY_CONTACT = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(4) div:nth-child(2)>'
      'div:nth-child(2)>div>input')
  UI_CONTROL_URL = (
      By.CSS_SELECTOR,
      '.modal-body form>div:nth-child(5) div:nth-child(2)>div:nth-child(1)>div'
      '>input')
  UI_REFERENCE_URL = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>form>div:nth-child(5) div:nth-child(2)>'
      'div:nth-child(2)>div>input')

  DATEPICKER_EFFECTIVE_DATE = (
      By.CSS_SELECTOR,
      '.modal-body div>form>div>div:nth-child(3)>div:nth-child(1) input')
  DATEPICKER_STOP_DATE = (
      By.CSS_SELECTOR,
      '.modal-body div>form>div>div:nth-child(3)>div:nth-child(2) input')

  # dorpdowns
  DROPDOWN_KIND_OR_NATURE = _Locator.get_dropdown_item(2, 1)
  DROPDOWN_FRAUD_RELATED = _Locator.get_dropdown_item(2, 2)
  DROPDOWN_SIGNIFICANCE = _Locator.get_dropdown_item(2, 3)
  DROPDOWN_TYPE_OR_MEANS = _Locator.get_dropdown_item(2, 4)
  DROPDOWN_FREQUENCY = _Locator.get_dropdown_item(4, 1)
  DROPDOWN_STATE = _Locator.get_dropdown_item(5, 3)

  SELECTABLE_ASSERTIONS = _Locator.get_dropdown_item(4, 2)
  SELECTABLE_CATEGORIES = _Locator.get_dropdown_item(4, 3)

  # buttons
  BUTTON_ADD_OWNER = (By.CSS_SELECTOR, 'isolate-form .btn')
  BUTTON_HIDE_ALL_OPTIONAL_FIELDS = (By.CSS_SELECTOR, '#formHide')


class ModalCreateNewIssue(BaseModalCreateNew):
  """Locators for the issue modal visible when creating a new modal from
  LHN"""


class ModalCreateNewRequest(BaseModalCreateNew):
  """Locators for the request modal visible when creating a new modal from
  LHN"""


class ModalEditObject(BaseModalCreateNew):
  """Locators for a generic edit object modal"""
  BUTTON_DELETE = (
      By.CSS_SELECTOR, '.deny-buttons [data-toggle="modal-ajax-deleteform"]')


class ModalCreateNewObject(BaseModalCreateNew):
  """Locators for a generic new object modal"""
  UI_TITLE = (By.CSS_SELECTOR, '[data-id="title_txtbx"]')

  BUTTON_SAVE_AND_CLOSE = (
      By.CSS_SELECTOR,
      '.modal-footer .confirm-buttons [data-toggle="modal-submit"]')
  BUTTON_SAVE_AND_ADD_ANOTHER = (
      By.CSS_SELECTOR,
      '.confirm-buttons [data-toggle="modal-submit-addmore"]')


class ModalCustomAttribute(object):
  """Locators for a generic custom attributes modal in admin dashboard"""

  MODAL_TITLE = (By.CSS_SELECTOR, '.modal-header h2')
  ATTRIBUTE_TITLE = (By.CSS_SELECTOR, '.modal-body div:nth-child(1)>label')
  INLINE_HELP = (By.CSS_SELECTOR, '.modal-body div:nth-child(2)>label')
  ATTRIBUTE_TYPE = (By.CSS_SELECTOR, '.modal-header h2')
  PLACEHOLDER = (By.CSS_SELECTOR, '.modal-header h2')
  MANDATORY = (By.CSS_SELECTOR, '.modal-header h2')
  UI_ATTRIBUTE_TITLE = (
      By.CSS_SELECTOR, '.modal-body div:nth-child(1)>input[tabindex="1"]')
  UI_INLINE_HELP = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>input[tabindex="4"]')
  UI_PLACEHOLDER = (By.CSS_SELECTOR, '.modal-body div:nth-child(2)>input')
  CHECKBOX_MANDATORY = (By.CSS_SELECTOR, '.modal-body [type="checkbox"]')
  BUTTON_ADD_ANOTHER = (
      By.CSS_SELECTOR,
      '.confirm-buttons [data-toggle="modal-submit-addmore"]')
  BUTTON_SAVE_AND_CLOSE = (
      By.CSS_SELECTOR,
      '.modal-footer .confirm-buttons [data-toggle="modal-submit"]')


class WidgetBar(object):
  """Locators for the bar containing the widgets/tabs"""

  class _Locator(object):
    @staticmethod
    def get_widget(object_name):
      return (By.CSS_SELECTOR, '[href="#{}_widget"]'.format(object_name))

  class __metaclass__(type):
    def __init__(self, *args):
      for object_singular, object_plural in zip(objects.ALL_SINGULAR,
                                                objects.ALL_PLURAL):
        name = object_singular.lower()
        setattr(self, object_plural, self._Locator.get_widget(name))

  BUTTON_ADD = (By.CSS_SELECTOR,
                '[data-test-id="button_widget_add_2c925d94"]')
  TAB_WIDGET = (By.CSS_SELECTOR, ".object-nav .active")
  ADMIN_PEOPLE = _Locator.get_widget("people_list")
  ADMIN_ROLES = _Locator.get_widget("roles_list")
  ADMIN_EVENTS = _Locator.get_widget("events_list")
  ADMIN_CUSTOM_ATTRIBUTE = _Locator.get_widget("custom_attribute")

  INFO = _Locator.get_widget("info")
  CUSTOM_ATTRIBUTES = _Locator.get_widget("custom_attribute")
  EVENTS = _Locator.get_widget("events_list")
  ROLES = _Locator.get_widget("roles_list")
  RISK_ASSESSMENTS = _Locator.get_widget("risk_assessment")
  TASKS = _Locator.get_widget("task")


class WidgetBarButtonAddDropdown(object):
  """Locators for the button/dropdown "add widget" in widget bar"""
  class _Locator(object):
    @staticmethod
    def get_dropdown_item(object_name):
      return (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                               '[href="#{}_widget"]'.format(object_name))

  class __metaclass__(type):
    def __init__(self, *args):
      for object_ in objects.ALL_PLURAL:
        name = object_.lower()
        setattr(self, object_, self._Locator.get_dropdown_item(name))

  THREAD_ACTORS = _Locator.get_dropdown_item("threat_actor")
  WORKFLOW_TASKS = _Locator.get_dropdown_item("workflow_task")


class ObjectWidget(object):
  """Locators for a generic widget"""

  CONTROL_COLUMN_TITLE = (
      By.CSS_SELECTOR, '.header .span4 .title-heading .widget-col-title')
  CONTROL_OWNER = (
      By.CSS_SELECTOR, '.header .span4 [data-field="contact.name|email"]')
  COTNROL_STATE = (
      By.CSS_SELECTOR, '.header .span4 [data-field="status"]')
  MEMBERS_TITLE_LIST = (
      By.CSS_SELECTOR,
      '.object-area .tree-structure .select .span4:nth-child(1)')
  INFO_PANE = (By.CSS_SELECTOR, '.sticky-info-panel')


class ModalDeleteObject(object):
  MODAL_TITLE = (By.CSS_SELECTOR, '.modal-header>h2')
  CONFIRMATION_TEXT = (By.CSS_SELECTOR, '.modal-body>div>p')
  OBJECT_TITLE = (By.CSS_SELECTOR, '.modal-body>div>p>span')
  BUTTON_DELETE = (
      By.CSS_SELECTOR, '.modal-footer .confirm-buttons>[data-toggle="delete"]')


class BaseInfoWidget(object):
  """Locators that are common to all info widgets"""
  BUTTON_SETTINGS = (By.CSS_SELECTOR, '.info-pane-utility')
  TITLE = (By.CSS_SELECTOR, '[data-test-id="title_0ad9fbaf"] h6')
  TITLE_ENTERED = (By.CSS_SELECTOR, '[data-test-id="title_0ad9fbaf"] h3')


class WidgetInfoProgram(BaseInfoWidget):
  """Locators for the info program widget"""

  PERMALINK_ALERT = (By.CSS_SELECTOR, '.content>.flash>.alert-success')

  ALERT_LINK_COPIED = (By.CSS_SELECTOR, '.alert.alert-success')
  MODAL_DELETE = (By.ID, '[id="ajax-lhn_modal-javascript:--"]')
  MODAL_DELETE_CLOSE = (By.CSS_SELECTOR, '.lhn_modal .grcicon-x-grey')

  OBJECT_REVIEW = (By.CSS_SELECTOR,
                   '[data-test-id="title_review_0ad9fbaf"] h6')
  SUBMIT_FOR_REVIEW = (By.CSS_SELECTOR,
                       '[data-test-id="title_review_0ad9fbaf"] '
                       '[href="javascript://"]')
  DESCRIPTION = (By.CSS_SELECTOR,
                 '[data-test-id="title_description_7a906d2e"] h6')
  DESCRIPTION_ENTERED = (By.CSS_SELECTOR,
                         '[data-test-id="title_description_'
                         'content_7a906d2e"]')
  NOTES = (By.CSS_SELECTOR, '[data-test-id="title_notes_ef5bc3a71e88"] '
                            'h6')
  NOTES_ENTERED = (By.CSS_SELECTOR,
                   '[data-test-id="title_notes_ef5bc3a71e88"]>div')
  MANAGER = (By.CSS_SELECTOR, '[data-test-id="title_manager_7a906d2e"] '
                              'h6')
  MANAGER_ENTERED = (By.CSS_SELECTOR,
                     '[data-test-id="title_manager_7a906d2e"] '
                     '[data-test-id="text_manager_7a906d2e"]')
  PROGRAM_URL = (By.CSS_SELECTOR,
                 '[data-test-id="title_program_url_aa7d1a65"] h6')
  PROGRAM_URL_ENTERED = (By.CSS_SELECTOR,
                         '[data-test-id="text_program_url_aa7d1a65"]')
  REFERENCE_URL = (By.CSS_SELECTOR,
                   '[data-test-id="title_reference_url_aa7d1a65"]')
  REFERENCE_URL_ENTERED = (By.CSS_SELECTOR,
                           '[data-test-id="text_reference_url_aa7d1a65"]')
  TOGGLE_SHOW_ADVANCED = (By.CSS_SELECTOR,
                          '[data-test-id="button_advanced_cf47bc01"]')
  TOGGLE_SHOW_ADVANCED_ACTIVATED = (
      By.CSS_SELECTOR, '[data-test-id="button_advanced_cf47bc01"].active')
  CODE = (By.CSS_SELECTOR, '[data-test-id="title_code_cf47bc01"] h6')
  CODE_ENTERED = (By.CSS_SELECTOR,
                  '[data-test-id="title_code_cf47bc01"] p')
  EFFECTIVE_DATE = (By.CSS_SELECTOR,
                    '[data-test-id="title_effective_date_cf47bc01"] h6')
  EFFECTIVE_DATE_ENTERED = (By.CSS_SELECTOR,
                            '[data-test-id="title_effective_date_'
                            'cf47bc01"] p')
  STOP_DATE = (By.CSS_SELECTOR,
               '[data-test-id="title_stop_date_cf47bc01"] h6')
  STOP_DATE_ENTERED = (By.CSS_SELECTOR,
                       '[data-test-id="title_stop_date_cf47bc01"] p')
  STATE = (By.CSS_SELECTOR,
           '[dadata-test-id="new_program_button_save_and_new_86160053"'
           ' ta-test-id="title_state_0ad9fbaf"] h6')
  STATE_ENTERED = (By.CSS_SELECTOR,
                   '[data-test-id="title_state_value_0ad9fbaf"]')
  PRIMARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id="title_primary_'
                                      'contact_696de7244b84"] h6')
  PRIMARY_CONTACT_ENTERED = (
      By.CSS_SELECTOR, '[data-test-id="text_primary_contact_'
                       '696de7244b84"] [data-test-id="text_'
                       'manager_7a906d2e"]')
  SECONDARY_CONTACT = (
      By.CSS_SELECTOR, '[data-test-id="title_contacts_696de7244b84"] '
                       'h6:nth-child(2)')
  SECONDARY_CONTACT_ENTERED = (
      By.CSS_SELECTOR, '[data-test-id="text_secondary_contact_'
                       '696de7244b84"] [data-test-id="text_manager_'
                       '7a906d2e"]')
  PRIVATE_PROGRAM = (By.CSS_SELECTOR,
                     '[data-test-id="title_private_ec758af9"] h6')
  ICON_LOCK = (By.CSS_SELECTOR, '[data-test-id="icon_private_ec758af9"]')


class WidgetInfoRequest(BaseInfoWidget):
  """Locators for the request info widget"""


class WidgetInfoRisk(BaseInfoWidget):
  """Locators for the risk info widget"""


class WidgetInfoOrgGroup(BaseInfoWidget):
  """Locators for the org group info widget"""


class WidgetInfoIssue(BaseInfoWidget):
  """Locators for the org group info widget"""


class WidgetInfoRegulations(BaseInfoWidget):
  """Locators for the regulation info widget"""


class WidgetInfoWorkflow(BaseInfoWidget):
  """Locators for the workflow info widget"""


class WidgetInfoAudit(BaseInfoWidget):
  """Locators for the audit info widget"""


class WidgetInfoAssessment(BaseInfoWidget):
  """Locators for the assessment info widget"""


class WidgetInfoPolicy(BaseInfoWidget):
  """Locators for the regulation info widget"""


class WidgetInfoStandard(BaseInfoWidget):
  """Locators for the standard info widget"""


class WidgetInfoContract(BaseInfoWidget):
  """Locators for the contract info widget"""


class WidgetInfoClause(BaseInfoWidget):
  """Locators for the clause info widget"""


class WidgetInfoSection(BaseInfoWidget):
  """Locators for the section info widget"""


class WidgetInfoControl(BaseInfoWidget):
  """Locators for the control info widget"""


class WidgetInfoObjective(BaseInfoWidget):
  """Locators for the objective info widget"""


class WidgetInfoPeople(BaseInfoWidget):
  """Locators for the people info widget"""


class WidgetInfoVendor(BaseInfoWidget):
  """Locators for the vendor info widget"""


class WidgetInfoAccessGroup(BaseInfoWidget):
  """Locators for the access group info widget"""


class WidgetInfoSystem(BaseInfoWidget):
  """Locators for the system info widget"""


class WidgetInfoProcess(BaseInfoWidget):
  """Locators for the process info widget"""


class WidgetInfoProduct(BaseInfoWidget):
  """Locators for the product info widget"""


class WidgetInfoFacility(BaseInfoWidget):
  """Locators for the facility info widget"""


class WidgetInfoProject(BaseInfoWidget):
  """Locators for the project info widget"""


class WidgetInfoMarket(BaseInfoWidget):
  """Locators for the market info widget"""


class WidgetInfoDataAsset(BaseInfoWidget):
  """Locators for the data asset info widget"""


class WidgetInfoThreat(BaseInfoWidget):
  """Locators for the data asset info widget"""


class WidgetAdminRoles(object):
  """Locators for the roles widget on the admin dashboard"""

  class _Locator(object):
    @staticmethod
    def get_role(child_id):
      return (By.CSS_SELECTOR,
              '[id="roles_list_widget"] li:nth-child({}) .span8>div'
              .format(child_id))

    @staticmethod
    def get_scope(child_id):
      return (By.CSS_SELECTOR,
              '[id="roles_list_widget"] li:nth-child({}) .span4 '
              '.scope'.format(child_id))

  class __metaclass__(type):
    def __init__(self, *args):
      items = (
          "EDITOR", "GRC_ADMIN", "PROGRAM_EDITOR", "PROGRAM_OWNER",
          "PROGRAM_READER", "READER", "WORKFLOW_MEMBER", "WORKFLOW_OWNER")

      for id_, name in enumerate(items, start=2):
        setattr(self, attribute.ROLE + name, self._Locator.get_role(id_))
        setattr(self, attribute.SCOPE + name, self._Locator.get_scope(id_))


class WidgetInfoSettingsButton(object):
  """Locators for the control info widget"""
  TITLE_ENTERED = (By.CSS_SELECTOR, '[data-test-id="title_0ad9fbaf"]>h3')

  DROPDOWN_SETTINGS_EDIT = (
      By.CSS_SELECTOR,
      '[data-test-id="dropdown_settings_edit_f4b27aec"]')
  DROPDOWN_SETTINGS_PERMALINK = (
      By.CSS_SELECTOR,
      '[data-test-id="dropdown_settings_get_permalink_75e3bf91"]')
  DROPDOWN_SETTINGS_DELETE = (
      By.CSS_SELECTOR, '[data-test-id="dropdown_settings_delete_6a62eaaf"]')


class BaseWidgetGeneric(object):
  """Locators shared amongst non info&admin widgets"""
  _object_name = None

  class __metaclass__(type):
    """For sharing parametrized class attributes we simply define how a
    class should look like. Note that the same functionality can be
    implemented using properties though with more code."""
    def __init__(self, *args):
      self.TITLE = (
          By.CSS_SELECTOR, '#{}_widget .sticky-filter .filter-title h6'
            .format(self._object_name))
      self.TEXTFIELD = (
          By.CSS_SELECTOR,
          '#{}_widget .sticky-filter .filter-input'.format(self._object_name))
      self.BUTTON_SUBMIT = (
          By.CSS_SELECTOR,
          '#{}_widget .sticky-filter .filter-button [type="submit"]'
            .format(self._object_name))
      self.BUTTON_RESET = (
          By.CSS_SELECTOR,
          '#{}_widget .sticky-filter .filter-button [type="reset"]'
            .format(self._object_name))
      self.BUTTON_HELP = (
          By.CSS_SELECTOR,
          '#{}_widget .sticky-filter .filter-button  #page-help'
            .format(self._object_name))


class WidgetControls(BaseWidgetGeneric):
  """Locators for control widget"""
  _object_name = "control"


class WidgetProducts(BaseWidgetGeneric):
  """Locators for product widget"""
  _object_name = "product"


class WidgetProjects(BaseWidgetGeneric):
  """Locators for project widget"""
  _object_name = "project"


class WidgetSystems(BaseWidgetGeneric):
  """Locators for system widget"""
  _object_name = "system"


class WidgetDataAssets(BaseWidgetGeneric):
  """Locators for system widget"""
  _object_name = "data_asset"


class WidgetProcesses(BaseWidgetGeneric):
  """Locators for system widget"""
  _object_name = "process"


class WidgetIssues(BaseWidgetGeneric):
  """Locators for system widget"""
  _object_name = "issue"


class AdminCustomAttributes(object):
  """Locators for the widget custom attributes in admin dashboard"""

  class _Locator(object):
    @staticmethod
    def get_toggle(child_id):
      return (By.CSS_SELECTOR, '#custom_attribute_widget li:nth-child({}) '
              '.openclose'.format(child_id))

    @staticmethod
    def get_programs_label(child_id):
      return (
          By.CSS_SELECTOR,
          '.tree-structure li:nth-child(5) div thead>tr>th:nth-child({})'
            .format(child_id))

  class __metaclass__(type):
    def __init__(self, *args):
      items = (
          objects.WORKFLOWS, "RISK_ASSESSMENTS", objects.THREATS,
          objects.RISKS, objects.PROGRAMS, objects.AUDITS,
          objects.OBJECTIVES, objects.SECTIONS, objects.CONTROLS,
          objects.ISSUES, objects.ASSESSMENTS, objects.STANDARDS,
          objects.REGULATIONS, objects.POLICIES, objects.CONTRACTS,
          objects.CLAUSES, objects.REQUESTS, objects.VENDORS, objects.PEOPLE,
          objects.ACCESS_GROUPS, objects.ORG_GROUPS, objects.PRODUCTS,
          objects.MARKETS, objects.PROCESSES, objects.FACILITIES,
          objects.PROJECTS, objects.DATA_ASSETS, objects.SYSTEMS)

      for id_, name in enumerate(items, start=1):
        setattr(self,
                attribute.TOGGLE + name.upper(),
                self._Locator.get_toggle(id_))

  FILTER_INPUT_FIELD = (By.CLASS_NAME, 'filter-input')
  FILTER_BUTTON_SUBMIT = (By.CSS_SELECTOR, '.filter-button>[type="submit"]')
  FILTER_BUTTON_RESET = (By.CSS_SELECTOR, '.filter-button>[type="reset"]')

  # programs dropdown
  BUTTON_ADD_CUSTOM_PROGRAM_ATTR = (
      By.CSS_SELECTOR,
      '.tree-item:nth-child(5) [data-test-id="button_add-86eaf948"]')
  PROGRAMS_LABEL_ATTRIBUTE_NAME = _Locator.get_programs_label(1)
  PROGRAMS_LABEL_ATTRIBUTE_TYPE = _Locator.get_programs_label(2)
  PROGRAMS_LABEL_MANDATORY = _Locator.get_programs_label(3)
  PROGRAMS_LABEL_EDIT = _Locator.get_programs_label(4)
  LISTED_MEMBERS = (
      By.CSS_SELECTOR,
      '.tree-structure li:nth-child(5) div tbody>tr')
  BUTTON_LISTED_MEMBERS_EDIT = (
      By.CSS_SELECTOR,
      '.tree-structure li:nth-child(5) div tbody>tr>td>ul .fa-pencil-square-o')
