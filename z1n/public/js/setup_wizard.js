frappe.require("assets/erpnext/js/setup_wizard.js", function() {
    erpnext.setup.slides_settings[0].fields[0].options.push(
        { "label": __("Z1N"), "value": "Z1N" },
    );
});
