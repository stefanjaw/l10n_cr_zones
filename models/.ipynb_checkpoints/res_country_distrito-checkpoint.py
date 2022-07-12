# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Distrito(models.Model):
    _name = "res.country.distrito"
    _description = "res.country.distrito"

    name = fields.Char(string="Distrito Name")
    code = fields.Char(string="Distrito Code")
    comments = fields.Char(string="Distrito Comments")

    canton_id = fields.Many2one("res.country.canton", string="Canton")
    state_id = fields.Char(string='Provincia',related='canton_id.state_id.name', store=True)
    country_id = fields.Char(string='País',related='canton_id.state_id.country_id.name', store=True)
    
