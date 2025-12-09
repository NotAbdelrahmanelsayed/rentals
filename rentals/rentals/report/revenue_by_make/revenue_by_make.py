# Copyright (c) 2025, Abdelrahman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [{
		"fieldname": "make",
		"label": "Make",
		"fieldtype": "Data"},
		{
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldtype": "Data"}
	]
	data = frappe.get_all("Ride Booking", 
					fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], 
					filters={"docstatus":("=",  1)}, group_by="make")

	chart = {
		"data": {
			"labels" :[x.make for x in data],
			"dataset": [{"values": [x.total_revenue for x in data]}],
		},
		"type": "pie",
	}
	return columns, data, "Revenue per car!", chart