# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime

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
    email_sent = fields.Datetime(string="Email Sent", tracking=True)

    @api.model
    def create(self, vals):
        # the end date must be later than the current time/date.
        if vals['end_date'] < str(datetime.now()):
            raise ValidationError(_("A booking cannot be made in the past"))

        vals['ref'] = self.env['ir.sequence'].next_by_code('cs_car_pool_booking.sequence')

        # Check to see if there are already bookings for this vehicle with overlapping dates
        booking_count = self.env['cs_car_pool.bookings'].search_count([
            ('start_date', '>=', vals['start_date']),
            ('end_date', '<=', vals['end_date']),
            ('vehicle_id', '=', vals['vehicle_id'])])
        if booking_count:
            raise ValidationError(
                _("There appears to be an active booking for this vehicle at that time"))

        return super(Cs_car_poolBookings, self).create(vals)

    def action_send_booking_email(self):
        template = self.env.ref('cs_car_pool.car_pool_booking_template')
        for rec in self:
            if rec.driver_id.work_email:
                template.send_mail(rec.id, force_send=True)
                rec.email_sent = datetime.now()
            else:
                raise ValidationError(_("Could not send email. Driver does not have an email address set on employee record"))
