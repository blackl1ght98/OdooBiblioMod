# -*- coding: utf-8 -*-
from odoo import models, fields

class Biblioteca(models.Model):
    _name = 'modulogfb.biblioteca'
    _description = 'Biblioteca'

    name = fields.Char(string='Nombre', required=True)
    capacidad = fields.Integer(string='Capacidad')
    libro_ids = fields.One2many(
        comodel_name='modulogfb.libro',
        inverse_name='biblioteca_id',
        string='Libros'
    )