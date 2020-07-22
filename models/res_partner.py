# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    country_id_code = fields.Char(string='Country Code',related='country_id.code', store=True)

    canton_id = fields.Many2one("res.country.canton", string="Canton")
    canton_id_comments = fields.Char(related='canton_id.comments')

    distrito_id = fields.Many2one("res.country.distrito", string="Distrito")
    distrito_id_comments = fields.Char(related='distrito_id.comments')

    barrio_id = fields.Many2one("res.country.barrio", string="Barrio")
    barrio_id_comments = fields.Char(related='barrio_id.comments')
    
