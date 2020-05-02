# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RepCovid(models.Model):
    _name = 'rep.covid'
    _description = 'rep.covid'

    fecha_hora = fields.Datetime()
    rep_covid_linea = fields.Many2many("rep.covid.linea", string="Unidades Militares")

