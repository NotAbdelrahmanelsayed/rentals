import frappe

@frappe.whitelist(allow_guest=True)
def get_request():
    return "This request is returned from rentals.rentals.api.get_request a white listed api"

def throw_emoji(doc, event):
    frappe.throw("♥")

def send_payment_remainders():
    pass