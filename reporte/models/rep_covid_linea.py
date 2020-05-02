# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RepCovidLinea(models.Model):
    _name = 'rep.covid.linea'
    _description = 'rep.covid.linea'

    unidad_id = fields.Many2one('rep.unidad', string='Unidad', required=True)
    ciudad_id = fields.Many2one('res.city', string='Ciudad', ondelete="restrict",
                                domain="[('unidad_id', '=?', unidad_id)]")
    cama_disponible = fields.Integer("Camas Disponibles", default=0, index=True)
    cuarentena_of_m = fields.Integer()
    cuarentena_of_f = fields.Integer()
    aislamiento_of_m = fields.Integer()
    aislamiento_of_f = fields.Integer()
