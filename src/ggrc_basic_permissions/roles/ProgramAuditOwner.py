# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

"""A module with configuration of the ProgramAuditOwner role's permissions."""

# pylint: disable=invalid-name


scope = "Audit Implied"
description = """
  A user with the ProgramOwner role for a private program will also have this
  role in the audit context for any audit created for that program.
  """
permissions = {
    "read": [
        "Request",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "UserRole",
        "Audit",
        "AuditObject",
        "Meeting",
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "Context",
    ],
    "create": [
        "Request",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "UserRole",
        "Audit",
        "AuditObject",
        "Meeting",
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting"
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        "Request",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "UserRole",
        "Audit",
        "AuditObject",
        "Meeting",
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting"
    ],
    "delete": [
        "UserRole",
        "Request",
        "Assessment",
        "AssessmentTemplate",
        "Issue",
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting"
        "AuditObject",
        "Audit"
    ]
}
