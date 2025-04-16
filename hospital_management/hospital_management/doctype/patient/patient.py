import frappe
from frappe.model.document import Document

class Patient(Document):
    pass
# Path: custom_app/custom/doctype/patient/patient.py

@frappe.whitelist()
def patient_name_query(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql("""
        SELECT 
            name, patient_name
        FROM 
            `tabPatient`
        WHERE 
            patient_name LIKE %(txt)s
        LIMIT 20
    """, {
        "txt": f"%{txt}%"
    })
