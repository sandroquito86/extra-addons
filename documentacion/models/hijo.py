from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api

class Hijo(models.Model):
    _name = 'hijo.hijo'
    _description = 'hijo.hijo'
    

    
    name = fields.Char(
        string='Nombre',
    )

    
    edad = fields.Integer(
        string='Edad',
    )
    
    