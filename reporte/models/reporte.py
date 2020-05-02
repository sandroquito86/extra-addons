# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reporte(models.Model):
    _name = 'reporte.reporte'
    _description = 'reporte.reporte'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    pais_id = fields.Many2one('res.country', string='Pais', ondelete='restrict')
    provincia_id = fields.Many2one("res.country.state", string="Provincia", ondelete="restrict",
                                   domain="[('country_id', '=?', pais_id)]")
    ciudad_id = fields.Many2one("res.city", string="Ciudad", ondelete="restrict",
                                domain="[('state_id', '=?', provincia_id)]")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100