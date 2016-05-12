/*!
    Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
    Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
    Created By: brad@reciprocitylabs.com
    Maintained By: brad@reciprocitylabs.com
*/

(function(can, $, CMS, GGRC) {

  var scopes = new can.Observe.List(['https://www.googleapis.com/auth/userinfo.email']);


  new GGRC.Mappings("ggrc_gdrive_integration", {
    folderable : {
      _canonical : {
        folders : "GDriveFolder"
      },
      object_folders: new GGRC.ListLoaders.DirectListLoader("ObjectFolder", "folderable", "object_folders"),
      folders: new GGRC.ListLoaders.ProxyListLoader("ObjectFolder", "folderable", "folder", "object_folders", "GDriveFolder")
    },

    fileable : {
      _canonical : {
        files : "GDriveFile"
      },
      files : new GGRC.ListLoaders.ProxyListLoader("ObjectFile", "fileable", "file", "object_files", "GDriveFile")
    },

    revisionable : {
      _canonical : {
        revisions : "GDriveFileRevision"
      },
      revisions : new GGRC.ListLoaders.DirectListLoader("GDriveFileRevision", "id")
    },

    Program : {
      _mixins : ["folderable"]
    },
    Audit : {
      _mixins : ["folderable"],
      extended_folders: new GGRC.ListLoaders.MultiListLoader(["folders"]),
      folders: new GGRC.ListLoaders.ProxyListLoader("ObjectFolder", "folderable",
        "folder", "object_folders", "GDriveFolder")
    },
    Request : {
      folders : new GGRC.ListLoaders.CrossListLoader("_audit", "folders"),
      _audit : new GGRC.ListLoaders.DirectListLoader("Audit", "requests", "audit"),
      extended_folders: new GGRC.ListLoaders.CrossListLoader("audits", "folders")
    },
    Assessment: {
      audits: GGRC.MapperHelpers.TypeFilter("related_objects", "Audit"),
      folders : new GGRC.ListLoaders.CrossListLoader("audits", "folders"),
      extended_folders: new GGRC.ListLoaders.CrossListLoader("audits", "folders")
    },
    Document : {
      _mixins : ["fileable"]
    },
    Meeting : {
      _canonical : {
        "events" : "GCalEvent"
      },
      events : new GGRC.ListLoaders.ProxyListLoader("ObjectEvent", "eventable", "event", "object_events", "GCalEvent")
    },
    Workflow: {
      _mixins :  ["folderable"],
      folders : new GGRC.ListLoaders.ProxyListLoader("ObjectFolder", "folderable", "folder", "object_folders", "GDriveFolder"),
      orphaned_objects : new GGRC.ListLoaders.MultiListLoader(["cycles", "task_groups", "tasks", "current_task_groups", "current_tasks", "folders"])
    },
    CycleTaskEntry : {
      folders : new GGRC.ListLoaders.CrossListLoader("workflow", "folders"),
      extended_folders : new GGRC.ListLoaders.MultiListLoader(["folders"])
    },
    GDriveFolder : {
      _mixins : ["revisionable"],
      _canonical : {
        permissions : "GDriveFolderPermission"
      },
      permissions : new GGRC.ListLoaders.DirectListLoader("GDriveFolderPermission", "id")
    },
    GDriveFile : {
      _mixins : ["revisionable"],
      _canonical : {
        permissions : "GDriveFilePermission"
      },
      permissions : new GGRC.ListLoaders.DirectListLoader("GDriveFilePermission", "id")
    }
  });

  GGRC.gapi_request_with_auth = $.proxy(GGRC.Controllers.GAPI, "gapi_request_with_auth");
  $(function() {
    $(document.body).ggrc_controllers_gapi({ scopes : scopes });
  });

  // set up a temporary global auth function so the GAPI onload can find it
  var r = Math.floor(Math.random() * 100000000);
  window["resolvegapi" + r] = function(gapi) {
    GGRC.Controllers.GAPI.gapidfd.resolve(gapi);
    delete window["resolvegapi" + r];
  };
  $('head').append("<script type='text/javascript' src='https://apis.google.com/js/client.js?onload=resolvegapi" + r + "'></script>");


  $.extend(true, CMS.Models.Audit.attributes, {
    "object_folders" : "CMS.Models.ObjectFolder.stubs"
    , "folders" : "CMS.Models.GDriveFolder.stubs"
  });

  can.view.mustache("picker-tag-default", "<ggrc-gdrive-folder-picker {{^is_allowed 'update' instance context='for'}}readonly=true{{/is_allowed}} instance='instance'/>");
  GGRC.register_hook("Audit.tree_view_info", "picker-tag-default");
  GGRC.register_hook("Audit.storage_folder_picker", GGRC.mustache_path + "/audits/gdrive_folder_picker.mustache");


  $.extend(true, CMS.Models.Document.attributes, {
    "object_files": "CMS.Models.ObjectFile.stubs",
    "files": "CMS.Models.GDriveFile.stubs"
  });

  can.view.mustache("picker-tag-readonly", "<ggrc-gdrive-folder-picker instance='instance' readonly='true'/>");
    //We are no longer mapping GDrive files directly to responses.  It makes it difficult to figure out which GDrive file is which
  // document when we go to present. however, this functionality is still supported.


  // GGRC.JoinDescriptor.from_arguments_list([
  //   [["Program", "Audit", "Request"], "GDriveFolder", "ObjectFolder", "folder", "folderable"]
  //   , ["GDriveFile", "ObjectFile", "file", "fileable"]
  // ]);

  $.extend(true, CMS.Models.Meeting.attributes, {
    "object_events" : "CMS.Models.ObjectEvent.stubs"
    , "events" : "CMS.Models.GCalEvent.stubs"
  });
  GGRC.register_hook("Meeting.tree_view_info", GGRC.mustache_path + "/meetings/gcal_info.mustache");

  GGRC.register_hook("Role.option_detail", GGRC.mustache_path + "/roles/gdrive_option_detail.mustache");

  // Enable these hooks when the deployment allows G+ APIs
  // GGRC.register_hook("Person.popover_actions", GGRC.mustache_path + "/people/gplus_actions.mustache");
  // GGRC.register_hook("Person.popover_info", GGRC.mustache_path + "/people/gplus_photo.mustache");

  GGRC.register_hook("Workflow.storage_folder_picker", GGRC.mustache_path + "/workflows/gdrive_folder_picker.mustache");

  GGRC.register_hook("Request.gdrive_evidence_storage", GGRC.mustache_path + "/requests/gdrive_evidence_storage.mustache");
  GGRC.register_hook("Request.gdrive_comment_attachment", GGRC.mustache_path + "/requests/gdrive_comment_attachment.mustache");

})(this.can, this.can.$, this.CMS, this.GGRC);
