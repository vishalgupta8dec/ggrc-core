/*!
    Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
    Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
    Created By: ivan@reciprocitylabs.com
    Maintained By: ivan@reciprocitylabs.com
*/

(function (can, $) {
  'use strict';

  GGRC.Components('assessmentTemplates', {
    tag: 'assessment-templates',
    template: can.view(
      GGRC.mustache_path +
      '/components/assessment_templates/assessment_templates.mustache'
    ),
    scope: {
      binding: '@',
      responses: [],
      instance: null,
      templates: function () {
        var result = {};
        var responses = this.attr('responses');
        var noValue = {
          title: 'No template',
          value: ''
        };
        _.each(responses, function (response) {
          var type;
          var instance;

          if (!response.instance) {
            return;
          }
          instance = response.instance;
          type = instance.template_object_type;
          if (!result[type]) {
            result[type] = {
              group: type,
              subitems: []
            };
          }
          result[type].subitems.push({
            title: instance.title,
            value: instance.id + '-' + type
          });
        });
        return [noValue].concat(_.toArray(result));
      }
    },
    init: function () {
      var instance = this.scope.attr('instance');
      var binding = instance.get_binding(this.scope.attr('binding'));

      binding.refresh_instances().done(function (response) {
        this.scope.attr('responses', response);
      }.bind(this));
    }
  });
})(window.can, window.can.$);
