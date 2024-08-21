from frappe import _

__version__ = '0.0.1'

def get_default_lead_reminder_settings():
    """Get the default settings for the Lead Reminder app."""
    return {
        "reminder_field_label": _("Reminder"),
        "reminder_field_description": _("Set a reminder date for this lead"),
    }

def install_lead_reminder():
    """Install the Lead Reminder app."""
    create_reminder_field()

def create_reminder_field():
    """Create the Reminder field in the Lead doctype."""
    from frappe.custom.doctype.custom_field.custom_field import create_custom_field

    lead_doctype = "Lead"
    field_name = "reminder"
    field_label = get_default_lead_reminder_settings()["reminder_field_label"]
    field_description = get_default_lead_reminder_settings()["reminder_field_description"]

    custom_field = {
        "doctype": "Custom Field",
        "dt": lead_doctype,
        "fieldname": field_name,
        "fieldtype": "Datetime",
        "label": field_label,
        "description": field_description,
    }

    create_custom_field(custom_field)

def uninstall_lead_reminder():
    """Uninstall the Lead Reminder app."""
    remove_reminder_field()

def remove_reminder_field():
    """Remove the Reminder field from the Lead doctype."""
    from frappe.custom.doctype.custom_field.custom_field import delete_custom_field

    lead_doctype = "Lead"
    field_name = "reminder"

    delete_custom_field(lead_doctype, field_name)
