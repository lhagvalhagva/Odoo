
from odoo import models, fields, api


class aa_custom_sale_order_module(models.Model):
    _name = 'aa_custom_sale_order_module.aa_custom_sale_order_module'
    _description = 'aa_custom_sale_order_module.aa_custom_sale_order_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
