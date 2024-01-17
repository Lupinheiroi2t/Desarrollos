

from odoo import fields, models, _, _lt


class City(models.Model):
    _name = "city"
    _description = "City"

    name = fields.Char(String="City")