# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Barrio(models.Model):
    _name = "res.country.barrio"

    name = fields.Char(string="Barrio Name")
    code = fields.Char(string="Barrio Code")
    comments = fields.Char(string="Barrio Comments")    
    
    distrito_id = fields.Many2one("res.country.distrito", string="Distrito")
    canton_id = fields.Char(string='Canton',related='distrito_id.canton_id.name', store=True)
    state_id = fields.Char(string='Provincia',related='distrito_id.canton_id.state_id.name', store=True)
    country_id = fields.Char(string='País',related='distrito_id.canton_id.state_id.country_id.name', store=True)
    
