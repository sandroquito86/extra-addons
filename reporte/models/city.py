# -*- coding: utf-8 -*-

from odoo import models, fields, api


class City(models.Model):
    _inherit = 'res.city'

    valor = fields.Integer()
    unidad_militar = fields.Char()
    unidad_id = fields.Many2one('rep.unidad',
                                ondelete='cascade', string="Unidad", required=True)
