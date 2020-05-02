# -*- coding: utf-8 -*-
# from odoo import http


# class Documentacion(http.Controller):
#     @http.route('/documentacion/documentacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/documentacion/documentacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('documentacion.listing', {
#             'root': '/documentacion/documentacion',
#             'objects': http.request.env['documentacion.documentacion'].search([]),
#         })

#     @http.route('/documentacion/documentacion/objects/<model("documentacion.documentacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('documentacion.object', {
#             'object': obj
#         })
