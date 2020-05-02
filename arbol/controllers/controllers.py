# -*- coding: utf-8 -*-
# from odoo import http


# class Arbol(http.Controller):
#     @http.route('/arbol/arbol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arbol/arbol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arbol.listing', {
#             'root': '/arbol/arbol',
#             'objects': http.request.env['arbol.arbol'].search([]),
#         })

#     @http.route('/arbol/arbol/objects/<model("arbol.arbol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arbol.object', {
#             'object': obj
#         })
