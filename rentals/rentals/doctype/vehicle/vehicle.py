# Copyright (c) 2025, Abdelrahman and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def validate(self):
		super().validate()
		self.set_title()
	
	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"