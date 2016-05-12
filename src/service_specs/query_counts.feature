# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: brad@reciprocitylabs.com
# Maintained By: brad@reciprocitylabs.com

@wip
Feature: Requests should require a bounded number of queries

  Scenario Outline: A resource query requires fewer than some number of database queries
    Given nothing new
    And initialized query count for "<endpoint>"
    When GET of "<endpoint>" as "ignored_value"
    Then query count increment is less than "<max_query_count>"

  Examples: Endpoints and associated maximum query counts
      | endpoint                         | max_query_count |
      | /api/audits                      | 14              |
      | /api/categorizations             | -1              |
      | /api/controls                    | 12              |
      | /api/control_categories          | -1              |
      | /api/control_assertions          | -1              |
      | /api/control_risks               | 10              |
      | /api/data_assets                 | 10              |
      | /api/directives                  | -1              |
      | /api/directive_controls          | 10              |
      | /api/contracts                   | 10              |
      | /api/policies                    | 10              |
      | /api/regulations                 | 10              |
      | /api/standards                   | 10              |
      | /api/documents                   | 10              |
      | /api/facilities                  | 10              |
      | /api/markets                     | 10              |
#      | /api/meetings                    | 10              |
      | /api/objectives                  | 10              |
      | /api/object_documents            | 10              |
      | /api/object_people               | 10              |
      | /api/object_controls             | 10              |
      | /api/options                     | 10              |
      | /api/org_groups                  | 10              |
      | /api/people                      | 10              |
      | /api/products                    | 10              |
      | /api/projects                    | 10              |
      | /api/programs                    | 10              |
      | /api/program_directives          | 10              |
      | /api/relationships               | -1              |
      | /api/requests                    | 12              |
      | /api/risks                       | 10              |
      | /api/risky_attributes            | 10              |
      | /api/risk_risky_attributes       | 10              |
      | /api/sections                    | 10              |
      | /api/systems_or_processes        | -1              |
      | /api/systems                     | 10              |
      | /api/processes                   | 10              |
