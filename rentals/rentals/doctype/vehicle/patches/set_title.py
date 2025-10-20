import frappe

def execute():
    vehciles = frappe.db.get_all('Vehicle')

    for v in vehciles:
        vehicle = frappe.get_doc("Vehicle", v)
        vehicle.set_title()
        vehicle.save()
    frappe.db.commit()