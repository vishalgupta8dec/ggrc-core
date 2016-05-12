# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

scope = "AuditImplied"
description = """
  A user with the ProgramReader role for a private program will also have this
  role in the audit context for any audit created for that program.
  """
permissions = {
    "read": [
        "Request",
        "Comment",
        "Assessment",
        "Issue",
        "Audit",
        "AuditObject",
        "Meeting",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "UserRole",
        "Context",
    ],
    "create": [],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [],
    "delete": []
}
