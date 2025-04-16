import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry

@frappe.whitelist()
def make_payment_entry(reference_doctype, reference_name, party_type, party, amount):
    try:
        # Ensure the required fields are not empty
        if not all([reference_doctype, reference_name, party_type, party, amount]):
            frappe.throw("Missing required parameters")
        
        # Create a new Payment Entry document
        pe = frappe.new_doc("Payment Entry")
        pe.payment_type = "Receive"
        pe.party_type = party_type
        pe.party = party
        pe.company = frappe.db.get_value(reference_doctype, reference_name, "company")
        pe.posting_date = frappe.utils.today()
        pe.paid_amount = amount
        pe.received_amount = amount
        
        # Append references section
        pe.append("references", {
            "reference_doctype": reference_doctype,
            "reference_name": reference_name,
            "allocated_amount": amount
        })
        
        # Insert the document and commit transaction
        pe.insert(ignore_permissions=True)  # It automatically commits the transaction
        
        return pe.name  # Return the name of the created payment entry
    except Exception as e:
        # Handle any errors that occur during the process
