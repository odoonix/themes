import base64

from odoo import api, SUPERUSER_ID
from odoo.modules import get_module_resource

iconMap = {
    'Contacts': 'Contacts.png',
    'Link Tracker': 'Link Tracker.png',
    'Dashboards': 'Dashboards.png',
    'Sales': 'Sales.png',
    'Invoicing': 'Invoicing.png',
    'Inventory': 'Inventory.png',
    'Purchase': 'Purchase.png',
    'Calendar': 'Calendar.png',
    'CRM': 'CRM.png',
    'Note': 'Note.png',
    'Website': 'Website.png',
    'Point of Sale': 'Point of Sale.png',
    'Manufacturing': 'Manufacturing.png',
    'Repairs': 'Repairs.png',
    'Email Marketing': 'Email Marketing.png',
    'SMS Marketing': 'SMS Marketing.png',
    'Project': 'Project.png',
    'Surveys': 'Surveys.png',
    'Employees': 'Employees.png',
    'Recruitment': 'Recruitment.png',
    'Attendances': 'Attendances.png',
    'Time Off': 'Time Off.png',
    'Expenses': 'Expenses.png',
    'Maintenance': 'Maintenance.png',
    'Live Chat': 'Live Chat.png',
    'Lunch': 'Lunch.png',
    'Fleet': 'Fleet.png',
    'Timesheets': 'Timesheets.png',
    'Events': 'Events.png',
    'eLearning': 'eLearning.png',
    'Members': 'Members.png',
}

def setMenuIcons(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    menu_item = env['ir.ui.menu'].search([('parent_id', '=', False)])
    for menu in menu_item:
        if menu.name in iconMap:
            img_path = get_module_resource(
                'vw_theme_dark_mode', 'static', 'src', 'img', 'icons', iconMap[menu.name])
            menu.write({'web_icon_data': base64.b64encode(open(img_path, "rb").read())})

def test_pre_init_hook(cr):
    setMenuIcons(cr)

def test_post_init_hook(cr, registry):
    setMenuIcons(cr)

