# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api

class documentacion(models.Model):
    _name = 'documentacion.documentacion'
    _description = 'documentacion.documentacion'
    # ordenar lista
    _order="name"




    name = fields.Char(help="ayuda")


    # campo obligatorio
    value = fields.Integer(required=True)

    
    # el campo que contiene _compute_name se calcula automaticamente
    #por defecto tendra el readonly =True
    value2 = fields.Float(compute="_compute_name")


    #default nos permite definir texto o valores a una variable
    description = fields.Text(default="agregando texto por defecto")

    # la palabra string nos permite darle un nombre de etiqueta al campo
    #campo con valor por defecto llamando a una funcion
    var_unicode = fields.Char(string='Nombre',
    default='description'
    )

    #index provoca que se cree un indice en el campo especificado
    indice = fields.Integer(
        string='campo Indice',
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

    activar = fields.Boolean()

    #many2many
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    #CAMPO RELACIONADO
        # 1 many2one
    hijo = fields.Many2one(
        string='nombre del Hijo',
        comodel_name='hijo.hijo',
        ondelete='restrict',
    )

    
    edad = fields.Integer(
        string='Edad Relacionada a Hijo',        
        related='hijo.edad',
        readonly=True,
        store=True,
        
    )

    
    contador = fields.Integer(
        string='Contador', compute="get_contador"
    )

 
    pais_id = fields.Many2many(
     string='Fecha',
     comodel_name='res.city',
     relation='documentacion_fecha_rel'
    
    )
    
  
    

    state = fields.Selection(selection=[
            ('draft', 'Draft'),
            ('posted', 'Posted'),
            ('cancel', 'Cancelled')
        ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')
 


    def get_contador(self):
        #hace referencia a un objeto y permite contar en base a un criterio
        contar= self.env['documentacion.documentacion'].search_count([('hijo', '=?', self.hijo.id)])
        self.contador=contar

        #PERMITE HACER DEBUG EN ODOO
        #import wdb
        #wdb.set_trace()

       
           
    
    
    
   


   

    #ACCION DEL BOTON   
        #la funcion debe tener el mismo nombre del name= ""
    
    def abrir_hijo(self):
        #PERMITE ABRIR OTRA VISTA 
        a=5
     
        return {
            'name': ('Entenado xD'),
            'domain': [('id', '=?',self.hijo.id)],
            'res_model': 'hijo.hijo',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def postedaction(self):
        for record in self:
            record.state = 'posted'
    
    def draftaction(self):
        for record in self:
            record.state = 'draft'

    


            

    #SEARCH
    #  siempre nos va a devolver objetos enteros RECORDSET
    def busqueda_search(self):
        domain=[('id','<','15')]
        # nos retorna un recordset (lista)
        record= self.env['documentacion.documentacion'].search(domain)
        concatenar=""
        record[0].name="cambio de nombre"
        for valor in record:
            concatenar =concatenar + str(valor.name)
            concatenar= concatenar + " "
        #raise ValidationError("LOS NOMBRES SON {},{}".format(concatenar,record[0].name))


    #SEARCH_READ
    #  devuelve un diccionario de datos
    def busqueda_search_read(self):
        domain=[('id','<','15')]
        fields=['id','name']
        dic= self.env['documentacion.documentacion'].search_read(domain,fields)
        concatenar=""
        for datos in dic:
            concatenar=concatenar+str(datos.get('id'))
            concatenar=concatenar+"-"
            concatenar=concatenar+str(datos.get('name'))
            concatenar=concatenar+" "
        raise ValidationError("LOS ID SON {}".format(concatenar))


    #BROWSE
    #  buscamos por este metodo cuando conocemos el ID tb nos retorna un RECORDSET    
    def busqueda_browse(self):       
        # nos retorna un recordset (lista)
        record= self.env['documentacion.documentacion'].browse(1)        
        raise ValidationError("EL NOMBRE DEL ID 1 ES: {}".format(record.name))    
    
    def environment_self(self):
        #Uso de Write
            #record_ids = self.env['documentacion.documentacion'].search([('id', '>', '1')])
            #for record in record_ids:
            #    record.write({
            #        'name': 'CHANGE'
            #    })         
            #raise ValidationError("RECORD {},{}".format(str(record),record[0].name))
            
        
        #uso de search
            #domain=[('is_company', '=', True),('id', '!=', 10)]    
            #record0 = self.env['res.partner'].search(domain)
            #raise ValidationError("FUNCIONA ENV {}".format(str(record0)))
        
        #uso de ref
        #INVESTIGAR COMO FUNCIONA
            #record=self.env.ref("documentacion.form")
            #raise ValidationError("ENV {}".format(self.env.ref("documentacion.form").read()[0]))

        #retorna el LENGUAJE
            #raise ValidationError("LENGUAJE {}".format(str(self.env.lang)))

        #retorna el COMPANIA ACTUAL
        raise ValidationError("LENGUAJE {}".format(str(self.env.company)))

        #para limpiar la cache luego de hacer las operaciones crud excepto r se usa
            #self.invalidate_cache()

        

       



   
   
   
    # cuando salga del campo value realiza cambio en campo value2
    @api.depends('value')
    def _compute_name(self):
        
        for record in self:
            record.value2 = record.value
        _logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(record.value))
        print("ESO ES TODO {}".format(self.env['documentacion.documentacion']))
    
    #INSTANCIA DEL OBJETO
        # _logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(self.env['prueba.prueba']))
        
    #REGISTROS QUE CONTIENE EL ID DEL XML
        #_logger.info("ENTRANDO A LA FUNCION EL VALOR DE VALUE ES {}".format(self.env.ref('prueba.form')))
        
        
        

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



    
    domain=[('id','<','10')]
    

    

    

    

            
    


    
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

    def _get_user_image(self, cr, uid, ids, field, arg, context=None):
        res = {}
        ctx = {}
        records = self.browse(cr, uid, ids, context=context)
        for record in records:
            res[record.id] = record.user_id.pool.get('res.partner')._get_default_image(cr, uid, False, ctx, colorize=True)
        return res

