# -*- coding: utf-8 -*-
# from odoo import http


# class Test123(http.Controller):
#     @http.route('/test123/test123/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test123/test123/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test123.listing', {
#             'root': '/test123/test123',
#             'objects': http.request.env['test123.test123'].search([]),
#         })

#     @http.route('/test123/test123/objects/<model("test123.test123"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test123.object', {
#             'object': obj
#         })
