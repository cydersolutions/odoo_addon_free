# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Cs_car_pool_logHrEmployee(models.Model):
    _inherit = 'hr.employee'

    preferred_vehicle = fields.Many2one('cs_car_pool.vehicles', "Preferred Vehicle")