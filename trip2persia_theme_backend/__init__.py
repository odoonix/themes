from . import models

from odoo import api, SUPERUSER_ID


def _uninstall_cleanup(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['web_editor.assets'].reset_asset(
        '/trip2persia_theme_backend/static/src/colors.scss', 
        'web._assets_primary_variables'
    )