# -*- coding: utf-8 -*-
from odoo import api, fields, models
class Cs_car_poolBookings(models.Model):
    _name = "cs_car_pool.bookings"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Car Pool Bookings"
    _rec_name = 'ref'

    ref = fields.Char(string='Ref Number', default='New', tracking=True)
    start_date = fields.Datetime("Start", required=True, tracking=True)
    end_date = fields.Datetime("End", required=True, tracking=True)
    vehicle_id = fields.Many2one('cs_car_pool.vehicles', "Vehicle", required=True, tracking=True)
    driver_id = fields.Many2one('hr.employee', "Driver", required=True, tracking=True)

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('cs_car_pool_booking.sequence')
        return super(Cs_car_poolBookings, self).create(vals)
