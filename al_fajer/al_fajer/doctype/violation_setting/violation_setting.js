// Copyright (c) 2023, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("violation setting", "onload", function(frm) {
    frm.set_query("deduction", function() {
        return {
            "filters": {
                "type": "Deduction"
            }
        };
    });
    frm.set_query("deduction_refund", function() {
        return {
            "filters": {
                "type": "Earning"
            }
        };
    });
});