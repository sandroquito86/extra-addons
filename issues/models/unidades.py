# uncompyle6 version 3.6.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
# [GCC 9.2.1 20191008]
# Embedded file name: /opt/odoo/extra-addons/reportecovid19/models/unidades.py
# Size of source mod 2**32: 438 bytes
from odoo import models, fields, api

class reportecovid19(models.Model):
    _name = 'reportecovid19.unidades'
    _description = 'reportecovid19.unidades'
    fecha_reporte = fields.Date(string='Ingrese la Fecha')
    name = fields.Char(string='Nombre de la Unidad')
    city_id = fields.One2many('reportecovid19.ciudad', 'unidad_id', string='Ciudades', required=True)
# okay decompiling unidades.cpython-37.pyc
