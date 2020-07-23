# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Canton(models.Model):
    _name = "res.country.canton"

    name = fields.Char(string="Canton Name")
    code = fields.Char(string="Canton Code")
    comments = fields.Char(string="Comments")

    state_id = fields.Many2one("res.country.state", string="Provincia")
    country_id = fields.Char(string='País',related='state_id.country_id.name', store=True)
