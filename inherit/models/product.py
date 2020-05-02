# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api


class ProductTemplate(models.Model):
    
    _inherit = 'product.template'
    

    nuevocampo = fields.Char(
        string='Nuevo Campo',        
    
        help='necesitas ayuda'        
    )
    
    
       

    nuevocampoKanban = fields.Float(
        string='Nuevo Campo',        

        help='necesitas ayuda'        
    )

    # metodo default_get se ejecuta antes del CREATE   
    @api.model
    def default_get(self, fields):
        res = super(ProductTemplate, self).default_get(fields)
        #devuelve un diccionario
        res['name']="Sandro Quito Bermeo"      
        return res

    # se ejecuta luego al presionar GUARDAR CUANDO EL REGISTRO ES NUEVO 
    @api.model
    def create(self, values):          
        result = super(ProductTemplate, self).create(values)
        #devuelve el registro
        if result.sale_ok:
            result.sale_ok=False  
        #_logger.info("EJECUTANDO")             
        return result

        

    
    #se ejecuta al MODIFICAR UN REGISTRO
    #UPDATE  
    def write(self, values):
    # VALUES ES UN DICCIONARIO  
        result = super(ProductTemplate, self).write(values)  
        domain=[('id','=','10')]
        # nos retorna un recordset (lista)
        if 'name' in values: #validamos si existe cambio 
            for record in self:
                record.purchase_ok=False            
        else:
            _logger.info("NO HAY CAMBIO EN NAME {}".format(values))    

        documentacion= self.env['documentacion.documentacion'].search(domain)
        for registro in documentacion:
            registro.name="HERENCIA"
            
        return result
    

    
    

    
    
    
    
    
        
    


   
  
   
  
