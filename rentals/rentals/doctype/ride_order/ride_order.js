// Copyright (c) 2025, Abdelrahman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if (frm.doc.status != "Accepted") {
            frm.add_custom_button("Accept", () => {
                // Status --> Accepted
                frm.set_value("status", "Accepted");
                // Save the form 
                frm.save();
            }, "Actions")
    }
        if (frm.doc.status != "rejected"){
            frm.add_custom_button("Reject", () => {
                    // Status --> Accepted
                    frm.set_value("status", "Rejected");
                    // Save the form 
                    frm.save();
                }, "Actions")
            }


	},
});
