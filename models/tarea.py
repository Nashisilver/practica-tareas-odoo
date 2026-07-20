from odoo import models, fields


class Tarea(models.Model):
    _name = 'practica.tarea'
    _description = 'Tarea de práctica'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_limite = fields.Date(string='Fecha límite')
    hecho = fields.Boolean(string='Completada', default=False)
