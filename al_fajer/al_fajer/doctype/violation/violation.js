// Copyright (c) 2023, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on('Violation', {
	refresh: function (frm) {
		if(frm.is_new() && frm.is_dirty() || frm.is_new()){
			frm.toggle_display('override_deduction', 0)
		}
	},
	
	violation_category: function (frm) {
		if (!frm.doc.violation_category) {
			frm.set_value('violation_type', null);
		}
	},
	
	override_deduction: function (frm) {
		frm.toggle_enable('deduction', frm.doc.override_deduction)
	},
	before_save: function (frm) {
		frm.set_value('override_deduction', 0)
	},
	after_save: function(frm){
		frm.toggle_display('override_deduction', 1)
	}
});
cur_frm.fields_dict['violation_type'].get_query = function (doc) {
	return {
		filters: {
			"violation_category": cur_frm.get_field('violation_category').get_value()
		}
	}
}
