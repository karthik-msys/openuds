// Generated by CoffeeScript 1.12.7
(function() {
  gui.connectivity = {
    transports: new GuiElement(api.transports, "trans"),
    networks: new GuiElement(api.networks, "nets")
  };

  gui.connectivity.link = function(event) {
    "use strict";
    var clearDetails;
    clearDetails = function() {
      return $("#detail-placeholder").addClass("hidden");
    };
    api.templates.get("connectivity", function(tmpl) {
      gui.clearWorkspace();
      gui.appendToWorkspace(api.templates.evaluate(tmpl, {
        transports: "transports-placeholder",
        networks: "networks-placeholder",
        transport_info: 'transports-info-placeholder'
      }));
      gui.connectivity.transports.table({
        icon: 'transports',
        container: "transports-placeholder",
        rowSelect: "multi",
        onRefresh: function(tbl) {
          return clearDetails();
        },
        onRowDeselect: function(deselected, dtable) {
          if (dtable.rows({
            selected: true
          }).count() !== 1) {
            clearDetails();
          }
        },
        onRowSelect: function(selected) {
          if (selected.length > 1) {
            clearDetails();
            return;
          }
          clearDetails();
          $("#detail-placeholder").removeClass("hidden");
          $('#detail-placeholder a[href="#transports-info-placeholder"]').tab('show');
          return gui.methods.typedShow(gui.connectivity.transports, selected[0], '#transports-info-placeholder .well', gettext('Error accessing data'));
        },
        onData: function(data) {
          $.each(data, function(undefined_, value) {
            var v;
            if (value.allowed_oss !== '') {
              value.allowed_oss = ((function() {
                var i, len, ref, results;
                ref = value.allowed_oss;
                results = [];
                for (i = 0, len = ref.length; i < len; i++) {
                  v = ref[i];
                  results.push(v.id);
                }
                return results;
              })()).toString();
            }
          });
        },
        buttons: ["new_grouped", "edit", "delete", "xls", "permissions"],
        onNew: gui.methods.typedNew(gui.connectivity.transports, gettext("New transport"), gettext("Transport creation error")),
        onEdit: gui.methods.typedEdit(gui.connectivity.transports, gettext("Edit transport"), gettext("Transport saving error")),
        onDelete: gui.methods.del(gui.connectivity.transports, gettext("Delete transport"), gettext("Transport deletion error"))
      });
      gui.connectivity.networks.table({
        icon: 'networks',
        rowSelect: "multi",
        container: "networks-placeholder",
        buttons: ["new", "edit", "delete", "xls", "permissions"],
        onNew: gui.methods.typedNew(gui.connectivity.networks, gettext("New network"), gettext("Network creation error")),
        onEdit: gui.methods.typedEdit(gui.connectivity.networks, gettext("Edit network"), gettext("Network saving error")),
        onDelete: gui.methods.del(gui.connectivity.networks, gettext("Delete network"), gettext("Network deletion error"))
      });
    });
  };

}).call(this);
