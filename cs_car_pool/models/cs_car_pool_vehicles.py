# -*- coding: utf-8 -*-
from odoo import api, fields, models
class Cs_car_poolVehicles(models.Model):
    _name = "cs_car_pool.vehicles"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Car Pool Vehicles"

    name = fields.Char('Registration')
    veh_make = fields.Char('Make')
    veh_model = fields.Char('Model')
    veh_capacity = fields.Char('Engine Capacity')
    date_of_manufacture = fields.Date(string="Date of Manufacture")
    veh_last_reading = fields.Integer("Last Reading")
    active = fields.Boolean(default=True)
