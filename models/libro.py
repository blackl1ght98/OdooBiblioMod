# -*- coding: utf-8 -*-
from odoo import models, fields

class Libro(models.Model):
    _name = 'modulogfb.libro'
    _description = 'Libro'

    name = fields.Char(string='Nombre', required=True)
    publicado = fields.Date(string='Fecha de Publicación')
    precio = fields.Float(string='Precio')
    genero = fields.Selection(
        selection=[
            ('ficcion', 'Ficción'),
            ('novela', 'Novela'),
            ('poesia', 'Poesía')
        ],
        string='Género'
    )
    biblioteca_id = fields.Many2one(
        comodel_name='modulogfb.biblioteca',
        string='Biblioteca',
        help='Biblioteca donde está el libro'
    )
    autor_ids = fields.Many2many(
        comodel_name='modulogfb.autor',
        string='Autores'
    )