# Copyright (c) 2023, ARD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document


class ViolationAction(Document):
    def validate(self):
        if self.deduction_type == 'Deduction By Day' or self.deduction_type == 'Deduction By Percentage':
            if self.deduction_valuerate < 0:
                frappe.throw(_("Deduction Value or Rate Can not be negative"))
