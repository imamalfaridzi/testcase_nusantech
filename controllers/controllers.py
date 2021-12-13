# -*- coding: utf-8 -*-
# from odoo import http


# class TestcaseNusantech(http.Controller):
#     @http.route('/testcase_nusantech/testcase_nusantech/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testcase_nusantech/testcase_nusantech/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testcase_nusantech.listing', {
#             'root': '/testcase_nusantech/testcase_nusantech',
#             'objects': http.request.env['testcase_nusantech.testcase_nusantech'].search([]),
#         })

#     @http.route('/testcase_nusantech/testcase_nusantech/objects/<model("testcase_nusantech.testcase_nusantech"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testcase_nusantech.object', {
#             'object': obj
#         })
