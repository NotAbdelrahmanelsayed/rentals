# Copyright (c) 2025, Abdelrahman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Abdelrahman"
		test_driver.last_name = "Elsayed"
		test_driver.licence_number = "HJG12358791"
		test_driver.phone = "+201000488181"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Abdelrahman Elsayed")

	def test_full_name_correctly_set_when_last_name_not_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Abdelrahman"
		test_driver.licence_number = "HJG12358791"
		test_driver.phone = "+201000488181"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Abdelrahman")