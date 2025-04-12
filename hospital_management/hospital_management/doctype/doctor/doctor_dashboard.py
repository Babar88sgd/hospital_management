from frappe import _

def get_data():
    return {
        "fieldname": "doctor",
        "transactions": [
            {
                "label": _("Availability"),
                "items": ["Available Timing"]
            }
        ]
    }
