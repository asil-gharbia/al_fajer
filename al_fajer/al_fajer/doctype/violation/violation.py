# Copyright (c) 2023, ARD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import flt, today, getdate, add_years, time_diff, get_datetime_str
from frappe.utils import get_first_day, add_days, get_last_day
# from erpnext.payroll.doctype.salary_structure.salary_structure import SalaryStructure

class Violation(Document):

    def before_insert(self):
        if self.additional_salary_earning or self.additional_salary_deduction:
            frappe.throw(_("Not allow to amend a cancelled Violation"))

        dv = frappe.db.get_value(
            "Violation Type", self.violation_type, 'duration_of_the_violation')
        
        dd = frappe.db.get_value(
            "Violation Type", self.violation_type, 'duration_of_dropping_violation')
        
        # Dropping Violations check box.
        if not self.dropping_violations:
            
            violation_list = frappe.db.get_list(
                "Violation", 
                filters={
                    "docstatus": 1,
                    "employee": self.employee,
                    "violation_type": self.violation_type,
                    "posting_date": ["between",
                                    [
                                        # to check duration of dropping violation.
                                        add_days(self.posting_date, -(dd)),
                                        self.posting_date
                                    ]
                                    ]
                },
                order_by="posting_date")
            
            # Get last violation doctype frequency.
            if violation_list:
                violation_last_doc = violation_list[-1].name
                violation_last_doc_frq = frappe.db.get_value("Violation", violation_last_doc, 'frequency_count')
            else:
                violation_last_doc_frq = 0
            
            # check if duration of the violation exceeded.
            if violation_last_doc_frq >= dv:
                frappe.throw(_("This Employee exceeded the maximum limit for " + self.violation_type  + " violation!"))
            else:
                count = violation_last_doc_frq
        else:
            # Dropping Violations check = 1.
            count = 0

        
        count = count + 1
        self.frequency_count = count
        violation_type = frappe.get_doc('Violation Type', self.violation_type)
        violation_actions = violation_type.violation_action

        for action in violation_actions:
            if self.frequency_count == action.frequency:
                v_action = frappe.get_doc(
                    "Violation Action", action.violation_action)

                self.violation_action = action.violation_action
                self.deduction_type = v_action.deduction_type
                self.deduction_amountrate = v_action.deduction_valuerate or ''
                break

        violation_frequency = [va.frequency for va in violation_actions]

        violation_frequency.sort()
        target = count
        for i, f in enumerate(violation_frequency):
            if f > target:
                target = violation_frequency[i-1]
                break
            elif f == target:
                target = f
                break

        self.make_deduction(target, violation_actions)

    def on_cancel(self):
        salary_component = frappe.get_doc("violation setting")
        deduction_refund =  salary_component.deduction_refund 
        if not deduction_refund : 
            frappe.throw(_("Please setup the violation setting first"))
        else:
            doc = frappe.get_doc({
                "doctype": "Additional Salary",
                "employee": self.employee,
                "employee_name": self.employee_name,
                "payroll_date": today(),
                "salary_component": deduction_refund,
                "company": self.company,
                "type": "Earning",
                "amount": self.deduction,
                "overwrite_salary_structure_amount": 0

            })
            doc = doc.insert()
            doc.submit()
            frappe.db.set(self, 'additional_salary_earning', doc.name)
            frappe.db.commit()

        # if self.violation_type == "فصل" or self.violation_type == "عقوبة فصل":
        #     sep_doc = frappe.get_doc({ "doctype": "Employee Separation", "name" : self.separation_doc})
        #     if sep_doc.docstatus == 0:
        #         frappe.db.delete("Employee Separation", {"name" : self.separation_doc})
        #         frappe.db.commit()
         



    def on_submit(self):
        salary_component = frappe.get_doc("violation setting")
        deduction =  salary_component.deduction
        if not deduction : 
            frappe.throw(_("Please setup the violation setting first"))
        else:
            doc = frappe.get_doc({
                "doctype": "Additional Salary",
                "employee": self.employee,
                "employee_name": self.employee_name,
                "payroll_date": today(),
                "salary_component": deduction,
                "company": self.company,
                "type": "Deduction",
                "amount": self.deduction,
                "overwrite_salary_structure_amount": 0
            })
            doc = doc.insert()
            doc.submit()
            frappe.db.set(self, 'additional_salary_deduction', doc.name)
            frappe.db.commit()


            # 
            violation_list = frappe.db.get_list(
                "Violation", 
                filters={
                    "docstatus": 0,
                    "employee": self.employee,
                    "violation_type": self.violation_type,
                },
                order_by="posting_date")
            
            if violation_list:
                draft_violations = ""
                for d in violation_list:
                    draft_violations += f"<a href='/app/violation/{d.name}' style='color: var(--text-on-blue)'>{d.name}</a><br>"  
                
                frappe.throw(_("You have to submit all violations first: <br>" + draft_violations))
            else: 
                pass

        # if self.violation_type == "فصل" or self.violation_type == "عقوبة فصل":
        #     doc = frappe.new_doc('Employee Separation')
        #     doc.employee = self.employee
        #     doc.boarding_begins_on = self.posting_date
        #     doc.save()          
        #     Employee_Separation = f"<a href='/app/employee-separation/{doc.name}' style='color: var(--text-on-blue)'>{doc.name}</a><br>"  
        #     frappe.msgprint("Employee Separation created " + Employee_Separation)

        
        

    # give daily rate
    def get_daily_rate(self, employee, start_date, end_date):
        doc = self.get_salary(employee, start_date, end_date)
        return doc.base / 30
    
    # get the base salary for this emplyee from the last salary structure assignment active
    def get_salary(self, employee, start_date, end_date):

        salary_structure_assignment = frappe.db.get_list(
            "Salary Structure Assignment",
            filters = {
                "employee": employee,
                "docstatus": 1
            },
            order_by = "creation desc",
            limit = 1
        )
        if salary_structure_assignment:
            doc = frappe.get_doc('Salary Structure Assignment' , salary_structure_assignment[0].name)
            if doc.base is not None:
                return doc
            else:
                frappe.throw(
                    _("Please create Salary Structure for employee this {}".format(employee)))
        else:
                frappe.throw(
                    _("Please create Salary Structure for employee this {}".format(employee)))

    def make_deduction(self, target_frequency, violation_actions):
        daily = self.get_daily_rate(self.employee,
                                    get_first_day(self.posting_date),
                                    get_last_day(self.posting_date))

        for violation_action in violation_actions:
            if target_frequency == violation_action.frequency:
                va = frappe.get_doc('Violation Action',
                                    violation_action.violation_action)
                if va.deduction_type == 'Deduction By Day':
                    self.deduction = daily * int(va.deduction_valuerate)
                elif va.deduction_type == 'Deduction By Percentage':
                    self.deduction = daily * \
                        float(va.deduction_valuerate) / 100
                elif va.deduction_type == 'Fixed Amount':
                    self.deduction = int(va.deduction_valuerate)
                else:
                    self.deduction = 0
