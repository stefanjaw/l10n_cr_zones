# -*- coding: utf-8 -*-
# from odoo import http


# class L10nCrZones(http.Controller):
#     @http.route('/l10n_cr_zones/l10n_cr_zones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cr_zones/l10n_cr_zones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cr_zones.listing', {
#             'root': '/l10n_cr_zones/l10n_cr_zones',
#             'objects': http.request.env['l10n_cr_zones.l10n_cr_zones'].search([]),
#         })

#     @http.route('/l10n_cr_zones/l10n_cr_zones/objects/<model("l10n_cr_zones.l10n_cr_zones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cr_zones.object', {
#             'object': obj
#         })
