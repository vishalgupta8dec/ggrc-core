/*!
    Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
    Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
    Created By: anze@reciprocitylabs.com
    Maintained By: anze@reciprocitylabs.com
*/


can.Control("CMS.Controllers.InfoPin", {
  defaults: {
    view: GGRC.mustache_path + "/base_objects/info.mustache"
  }
}, {
  init: function (el, options) {
    var instance = GGRC.page_instance();
    this.element.height(0);
  },
  findView: function (instance) {
    var view = instance.class.table_plural + "/info";

    if (instance instanceof CMS.Models.Person) {
      view = GGRC.mustache_path + "/ggrc_basic_permissions/people_roles/info.mustache";
    } else if (view in GGRC.Templates) {
      view = GGRC.mustache_path + "/" + view + ".mustache";
    } else {
      view = this.options.view;
    }
    return view;
  },
  findOptions: function (el) {
    var tree_node = el.closest(".cms_controllers_tree_view_node").control();
    return tree_node.options;
  },
  loadChildTrees: function() {
    var child_tree_dfds = [],
        that = this;

    this.element.find("." + CMS.Controllers.TreeView._fullName).each(function (_, el) {
      var $el = $(el),
          child_tree_control;

      //  Ensure this targets only direct child trees, not sub-tree trees
      if ($el.closest("." + that.constructor._fullName).is(that.element)) {
        child_tree_control = $el.control();
        if (child_tree_control)
          child_tree_dfds.push(child_tree_control.display());
      }
    });
  },
  hideInstance: function () {
    this.element.stop(true);
    this.element.height(0).html("");
    $(window).trigger("resize");
  },
  unsetInstance: function () {
    this.element.stop(true);
    this.element.animate({
        height: 0
      }, {
        duation: 800,
        complete: function () {
          this.element.html("");
          $(".cms_controllers_tree_view_node").removeClass("active");
          $(window).trigger("resize");
        }.bind(this)
      });
  },
  setInstance: function (instance, el) {
    var options = this.findOptions(el),
        view = this.findView(instance),
        panelHeight = $(window).height() / 3;

    this.element.html(can.view(view, {
      instance: instance,
      model: instance.class,
      is_info_pin: true,
      options: options,
      result: options.result,
      page_instance: GGRC.page_instance()
    }));

    // Load trees inside info pin
    this.loadChildTrees();

    // Make sure pin is visible
    if (!this.element.height()) {
      this.element.animate({
        height: panelHeight
      }, {
        duration: 800,
        easing: "easeOutExpo",
        complete: function () {
          this.ensureElementVisible(el);
        }.bind(this)
      });
    } else {
      this.ensureElementVisible(el);
    }
  },
  ensureElementVisible: function (el) {
    $(window).trigger("resize");
    var $objectArea = $(".object-area"),
        $header = $(".tree-header:visible"),
        $filter = $(".filter-holder:visible"),
        elTop = el.offset().top,
        elBottom = elTop + el.height(),
        headerTop = $header.offset().top,
        headerBottom = headerTop + $header.height(),
        infoTop = this.element.offset().top;

    if (elTop < headerBottom || elBottom > infoTop) {
      el[0].scrollIntoView(false);
      if (elTop < headerBottom) {
        el[0].scrollIntoView(true);
        $objectArea.scrollTop($objectArea.scrollTop() - $header.height() - $filter.height());
      } else {
        el[0].scrollIntoView(false);
      }
    }
  },
  ".pin-action a click": function (el) {
    var $win = $(window),
        win_height = $win.height(),
        options = {
          duration: 800,
          easing: "easeOutExpo"
        },
        target_height =  {
          min: 75,
          normal: (win_height / 3),
          max: (win_height * 3 / 4)
        },
        $info = this.element.find(".info"),
        type = el.data("size"),
        size = target_height[type];

    if (type === "deselect") {
      // TODO: Make some direct communication between the components
      //       and make sure only one widget has "widget-active" class
      el.find("[rel=tooltip]").data("tooltip").hide();
      $(".widget-area .widget:visible").find(".cms_controllers_tree_view").control().deselect();
      this.unsetInstance();
      return;
    }
    this.element.find(".pin-action i").css({"opacity": 0.25});

    if (size < $info.height()) {
      options.start = function () {
        $win.trigger("resize", size);
      };
    } else {
      options.complete = function () {
        $win.trigger("resize");
      };
    }

    this.element.animate({height: size}, options);
    el.find("i").css({"opacity": 1});
  }
});

