# -*- coding: utf-8 -*-
from odoo import models, fields

class Autor(models.Model):
    _name = 'modulogfb.autor'
    _description = 'Autor'

    name = fields.Char(string='Nombre', required=True)
    nacionalidad = fields.Char(string='Nacionalidad')