# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class test123(models.Model):
#     _name = 'test123.test123'
#     _description = 'test123.test123'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
