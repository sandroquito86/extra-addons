# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api


class arbol(models.Model):
    _name = 'arbol.arbol'
    _description = 'arbol.arbol'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(compute="_nombre" , store=True)
    



    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) *10

    @api.depends('name')
    def _nombre(self):
        for record in self:   
            if record.name:     
                record.description = "Adrian Macancela"
            

