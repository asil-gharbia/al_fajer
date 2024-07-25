# Copyright (c) 2023, ARD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

import collections


class ViolationType(Document):
    def validate(self):
        if self.duration_of_the_violation <= 0:
            frappe.throw(_("Duration Can not be requla or less than 0"))
        
        if len(self.violation_action) != self.duration_of_the_violation:
             frappe.throw(_("Length of violation action must be equal to duration of violation!"))

        for va in self.violation_action:
            if va.frequency <= 0:
                frappe.throw(_('Frequencies Must Be > 0'))
            

        duplicated = [item for item,
                      count in collections.Counter([va.frequency for va in self.violation_action]).items() if count > 1]
        if duplicated:
            frappe.throw(_('Duplicated Frequencies Not Allowed'))
