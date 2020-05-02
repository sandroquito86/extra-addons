# uncompyle6 version 3.6.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
# [GCC 9.2.1 20191008]
# Embedded file name: /opt/odoo/extra-addons/reportecovid19/models/detalle_reporte.py
# Size of source mod 2**32: 655 bytes
from odoo import models, fields, api

class RepCovidLinea(models.Model):
    _name = 'reportecovid19.detalle'
    _description = 'reportecovid19.detalle'
    unidad_id = fields.Many2one('reportecovid19.unidades', string='Unidad', required=True)
    ciudad_id = fields.Many2one('reportecovid19.ciudad', string='Ciudad', ondelete='restrict', domain="[('unidad_id', '=?', unidad_id)]")
    cama_disponible = fields.Integer('Camas Disponibles', default=0, index=True)
    cuarentena_of_m = fields.Integer()
    cuarentena_of_f = fields.Integer()
    aislamiento_of_m = fields.Integer()
    aislamiento_of_f = fields.Integer()
# okay decompiling detalle_reporte.cpython-37.pyc
