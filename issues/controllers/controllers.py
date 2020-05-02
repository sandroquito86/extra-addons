# -*- coding: utf-8 -*-
# from odoo import http


# class Issues(http.Controller):
#     @http.route('/issues/issues/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/issues/issues/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('issues.listing', {
#             'root': '/issues/issues',
#             'objects': http.request.env['issues.issues'].search([]),
#         })

#     @http.route('/issues/issues/objects/<model("issues.issues"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('issues.object', {
#             'object': obj
#         })
