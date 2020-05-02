# -*- coding: utf-8 -*-

from odoo import fields, models


class RepUnidad(models.Model):
    _name = 'rep.unidad'
    _description = 'Unidad'

    name = fields.Char("Unidad", required=True, translate=True)

    country_id = fields.Many2one('res.country', string='Pais', required=True)
    state_id = fields.Many2one(
        'res.country.state', 'Provincia', domain="[('country_id', '=', country_id)]", required=True)
    city_id = fields.One2many('res.city', 'unidad_id', string='Ciudades', required=True)
