# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

scope = "Audit"
description = """
  The permissions required by an auditor to access relevant resources for the
  program being audited.
  """
permissions = {
    "read": [
        "Audit",
        "Request",
        "Assessment",
        "Issue",
        "Meeting",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "UserRole",
        "Comment",
        "Context",
    ],
    "create": [
        "Request",
        "Assessment",
        "Issue",
        "Relationship",
        "Comment",
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        "Request",
        "Assessment",
        "Issue",
        "Comment"
    ],
    "delete": [
        "Request",
        "Assessment",
        "Issue"
    ],
}
