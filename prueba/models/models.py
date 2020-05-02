# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api



class prueba(models.Model):
    _name = 'prueba.prueba'
    _description = 'prueba.prueba'
    # _rec_name me permite cambiar el name por defecto que necesita cada tabla

    name = fields.Char(help="ayuda")
    
    # campo obligatorio
    value = fields.Integer(required=True)

    # @api.depends('nombreCampo')
        # cuando salgamos del nombreCampo se realizara la operacion que se defina en la funcion
        # el campo que contiene _compute_name se calcula automaticamente
        #por defecto tendra el readonly =True
    value2 = fields.Float(compute="_compute_name")

    #default nos permite definir texto o valores a una variable
    description = fields.Text(default="agregando texto por defecto")

    # la palabra string nos permite darle un nombre de etiqueta al campo
    var_unicode = fields.Char(
        string='Nombre'
    )

    #index provoca que se cree un indice en el campo especificado
    indice = fields.Integer(
        string='field_name',
        index=True        
    )
    
    #el numero estara compuesto por 4 numeros enteros y dos decimales
    # pero no funciona ahora que estoy probando XD
    duration = fields.Float(digits=(6, 2), help="Duration in days")

    #tipo de campo seleccion
    selection_field = fields.Selection(
        string='field_name',
        selection=[('valor1', 'valor1'), ('valor2', 'valor2')]
    )

    #many2many
    attendee_ids = fields.Many2many('res.partner', string="Attendees")    

    activar = fields.Boolean()

 
    # cuando salga del campo value realiza cambio en campo name
    @api.depends('value')
    def _compute_name(self):
    #INSTANCIA DEL OBJETO
        # _logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(self.env['prueba.prueba']))
        
    #REGISTROS QUE CONTIENE EL ID DEL XML
        #_logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(self.env.ref('prueba.form')))
        
        
        for record in self:
            record.value2 = record.value
        _logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(record.value))

    # este decorador se activa cuando se realice un cambio en los campos definidos
    @api.onchange('name','var_unicode')
    def _onchange_field(self):
        if self.name:
            self.value = 100
        if self.var_unicode:
            self.value = 200
        
    # permite definir reglas de validacion en el momento de guardar la informacion
        
    _sql_constraints = [
        ('name_description_check',
         'CHECK (name != var_unicode)',
         "debe ser diferente"),

        ('name_unique',
         'UNIQUE(name)',
         "El nombre debe ser unico"),
    ]

    # validacion por medio de un decorador
    @api.constrains('value')
    def _check_something(self):
        for record in self:
            if record.value < 20:
                raise ValidationError("el campo valor debe ser mayor a 20: ")

    
            
    


    
    #INFORMACION QUE CONTIENE SELF 
    """
    The object self.env gives access to request parameters and other useful things:

    self.env.cr or self._cr is the database cursor object; it is used for querying the database
    self.env.uid or self._uid is the current user’s database id
    self.env.user is the current user’s record
    self.env.context or self._context is the context dictionary
    self.env.ref(xml_id) returns the record corresponding to an XML id
    self.env[model_name] returns an instance of the given model
    """


    


  