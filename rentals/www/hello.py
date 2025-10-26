import frappe 
import pandas as pd
def get_context(context):
    context.my_doc = pd.Series(frappe.get_last_doc("Vehicle").as_dict())
    context.my_secret_name = "Not Abdelrahman"

    return context