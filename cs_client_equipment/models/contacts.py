# -*- coding: utf-8 -*-

#################################################################################
# Author      : Cyder Solutions (<www.cyder.com.au>)
# Copyright(c): 2021-now
# All Rights Reserved.
#
# This module is copyright property of the author mentioned above.
# You can't redistribute/reshare/recreate it for any purpose.
#
#################################################################################

from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"


    site_contact = fields.Char(string="Site Contact")

    site_phone = fields.Char(string="Site Phone")




