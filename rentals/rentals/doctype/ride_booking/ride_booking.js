// Copyright (c) 2025, Abdelrahman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
    refresh(frm) {},

    rate(frm) {
        frm.trigger("update_total_amount");
    },

    update_total_amount(frm) {
        let total_d = 0;

        // Sum up distances from child table
        (frm.doc.items || []).forEach(item => {
            total_d += item.distance || 0;
        });

        const amount = (frm.doc.rate || 0) * total_d;

        // ✅ Correct usage: pass value inside set_value()
        frm.set_value("total_amount", amount);
    },
});

frappe.ui.form.on("Ride Booking Item", {
    distance(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    },

    source(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    },

    destination(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    },
    
});
