import frappe
from frappe.model.document import Document

class Patient(Document):
    pass

def get_dashboard_data():
    return {
        'transactions': [
            {
                'label': __('Connections'),
                'items': [
                    'Patient Appointment',
                    'Billing',
                    'Prescription',
                ]
            }
        ]
    }
