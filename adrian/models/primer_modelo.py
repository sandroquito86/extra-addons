# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adrian(models.Model):
    _name = 'adrian.adrian'
    _description = 'adrian.adrian'

    name = fields.Char(
    string='Nombre'
    )
    value = fields.Integer()
    value2 = fields.Float(compute="_multiplicar", store=True)
    description = fields.Text()

    
    edad = fields.Integer(
        string='Edad',
    )
    
    
   
    




    @api.depends('value')
    def _multiplicar(self):
        for record in self:
            record.value2 = float(record.value) / 100



    