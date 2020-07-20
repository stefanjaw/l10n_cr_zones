# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    canton_id = fields.Many2one("res.country.canton", string="Canton")
    distrito_id = fields.Many2one("res.country.distrito", string="Distrito")
    barrio_id = fields.Many2one("res.country.barrio", string="Barrio")
    
    country_id_code = fields.Char(string='Country Code',related='country_id.code', store=True)
    