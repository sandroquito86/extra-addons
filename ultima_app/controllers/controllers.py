# -*- coding: utf-8 -*-
# from odoo import http


# class UltimaApp(http.Controller):
#     @http.route('/ultima_app/ultima_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ultima_app/ultima_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ultima_app.listing', {
#             'root': '/ultima_app/ultima_app',
#             'objects': http.request.env['ultima_app.ultima_app'].search([]),
#         })

#     @http.route('/ultima_app/ultima_app/objects/<model("ultima_app.ultima_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ultima_app.object', {
#             'object': obj
#         })
