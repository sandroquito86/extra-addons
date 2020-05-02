# uncompyle6 version 3.6.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
# [GCC 9.2.1 20191008]
# Embedded file name: /opt/odoo/extra-addons/reportecovid19/models/ciudad.py
# Size of source mod 2**32: 391 bytes
from odoo import models, fields, api

class ciudad(models.Model):
    _name = 'reportecovid19.ciudad'
    _description = 'reportecovid19.ciudad'
    name = fields.Char(string='Ciudades', required=True)
    unidad_militar = fields.Char()
    unidad_id = fields.Many2one('reportecovid19.unidades', ondelete='cascade',
      string='Unidad',
      required=True)
# okay decompiling ciudad.cpython-37.pyc
