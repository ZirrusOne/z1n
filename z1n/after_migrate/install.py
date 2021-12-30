import frappe


def execute():
    _setup_system_setting()
    _setup_website()


def _setup_system_setting():
    frappe.db.set_value('System Settings', None, 'app_name', 'Z1N')


def _setup_website():
    frappe.db.set_value('Website Settings', None, 'disable_signup', 1)
    frappe.db.set_value('Website Settings', None, 'hide_footer_signup', 1)
    frappe.db.set_value('Website Settings', None, 'footer', '')
    frappe.db.set_value('Website Settings', None, 'copyright', '')
    frappe.db.delete('Top Bar Item', {'parent': 'Website Settings'})