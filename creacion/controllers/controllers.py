# -*- coding: utf-8 -*-
# from odoo import http


# class Creacion(http.Controller):
#     @http.route('/creacion/creacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/creacion/creacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('creacion.listing', {
#             'root': '/creacion/creacion',
#             'objects': http.request.env['creacion.creacion'].search([]),
#         })

#     @http.route('/creacion/creacion/objects/<model("creacion.creacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('creacion.object', {
#             'object': obj
#         })
