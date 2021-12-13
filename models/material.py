# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = "material"
    _description = "Material"


    code = fields.Char(
        string='Material Code',
        required=True
    )
    name = fields.Char(
        string='Material Name',
        required=True
    )
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')],
        string='Material Type',
        required=True,
    )
    buy_price = fields.Integer(
        string='Material Buy Price',
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Related Supplier',
        required=True
    )


    _sql_constraints = [
        ('code_uniq', 'unique (code)', _('The code must be unique !')),
    ]


    @api.constrains('buy_price')
    def _check_buy_price(self):
        if self.buy_price < 100:
            raise ValidationError(_('Error: Buy Price cannot less then `100`'))