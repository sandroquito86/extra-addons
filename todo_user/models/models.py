# -*- coding: utf-8 -*-

from odoo import models, fields, api


class todo_user(models.Model):
   _inherit = 'ultima_app.datos'
   user_id= field_name_id = fields.Many2one(
       'res.users',
       'responsible',
   )
   date_deadline = fields.Date('Deadline')
   campoIndice = fields.Char()

# se puede modificar campos existentes simplemente con el nombre del atributo heredado
   name = fields.Char(help="Necesitas ayuda sobre este campo")





   

