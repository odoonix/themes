from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # ----------------------------------------------------------
    # Fields
    # ----------------------------------------------------------

    background_image = fields.Binary(
        string="Apps Menu Background Image", attachment=True
    )
