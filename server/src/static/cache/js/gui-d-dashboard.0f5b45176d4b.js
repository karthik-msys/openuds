// Generated by CoffeeScript 1.12.7
(function() {
  gui.dashboard = new BasicGuiElement("Dashboard");

  gui.dashboard.link = function(event) {
    "use strict";
    gui.clearWorkspace();
    if (api.config.admin === true) {
      api.templates.get("dashboard", function(tmpl) {
        api.system.overview(function(data) {
          gui.doLog("enter dashboard");
          gui.appendToWorkspace(api.templates.evaluate(tmpl, {
            users: data.users,
            services: data.services,
            user_services: data.user_services,
            restrained_services_pools: data.restrained_services_pools
          }));
          gui.setLinksEvents();
          $.each(["assigned", "inuse"], function(index, stat) {
            api.system.stats(stat, function(data) {
              var d;
              d = [];
              $.each(data, function(index, value) {
                d.push([value.stamp * 1000, value.value]);
              });
              gui.doLog("Data", d);
              $.plot("#placeholder-" + stat + "-chart", [d], {
                xaxis: {
                  mode: "time",
                  timeformat: api.tools.djangoFormat(django.formats.SHORT_DATE_FORMAT)
                }
              });
            });
          });
        });
      });
    } else {
      api.templates.get("restricted", function(tmpl) {
        gui.appendToWorkspace(api.templates.evaluate(tmpl, {
          user: gettext('Staff member')
        }));
        return gui.setLinksEvents();
      });
    }
  };

}).call(this);