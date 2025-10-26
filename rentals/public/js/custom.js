frappe.ui.keys.add_shortcut({
  shortcut: 'shift+ctrl+alt+n',
  description: 'Create new record of current Doctype',
  action: () => {
    const r = frappe.get_route();

    // If you're on a List (e.g., ["List","Sales Invoice","List"])
    if (r[0] === 'List' && r[1]) {
      return frappe.new_doc(r[1]);
    }

    // If you're on a Form (e.g., ["Form","Sales Invoice","SINV-0001"])
    if (r[0] === 'Form' && r[1]) {
      return frappe.new_doc(r[1]);
    }

    // Fallback: open DocType creation
    return frappe.new_doc('DocType');
  }
});
