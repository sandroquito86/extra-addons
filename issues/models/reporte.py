# uncompyle6 version 3.6.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
# [GCC 9.2.1 20191008]
# Embedded file name: /opt/odoo/extra-addons/reportecovid19/models/reporte.py
# Size of source mod 2**32: 279 bytes
from odoo import models, fields, api

class RepCovid(models.Model):
    _name = 'reportecovid19.reporte'
    _description = 'reportecovid19.reporte'
    fecha_hora = fields.Datetime()
    rep_covid_linea = fields.Many2many('reportecovid19.detalle', string='Unidades Militares')
# okay decompiling reporte.cpython-37.pyc
