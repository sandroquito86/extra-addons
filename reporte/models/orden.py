# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orden(models.Model):
    _name = 'reporte.orden'
    _description = 'reporte.orden'

    nombre = fields.Char()
    invoice_line_ids = fields.Integer()
    reporte_id = fields.Many2many("reporte.reporte", string="Reporte")
    # fields.One2many('account.move.line', string='Invoice lines')

