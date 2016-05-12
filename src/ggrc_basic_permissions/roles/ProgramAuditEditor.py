# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

scope = "Audit Implied"
description = """
  A user with the ProgramEditor role for a private program will also have this
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
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "UserRole",
        "Context",
    ],
    "create": [
        "Request",
        "Comment",
        "Assessment",
        "Issue",
        "Meeting",
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "AuditObject"
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        {
            "type": "Assessment",
            "terms": {
                "list_property": "owners",
                "value": "$current_user"
            },
            "condition": "contains"
        },
        {
            "type": "Issue",
            "terms": {
                "list_property": "owners",
                "value": "$current_user"
            },
            "condition": "contains"
        },
        "Request",
        "Comment",
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
        "ObjectControl",
        "ObjectDocument",
        "ObjectPerson",
        "Relationship",
        "Document",
        "Meeting",
        "Audit",
        "AuditObject"
    ]
}
