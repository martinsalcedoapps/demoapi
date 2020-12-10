# -*- coding: utf-8 -*-
from odoo import http
import json

class Demoapi(http.Controller):

    @http.route('/demoapi/', auth='public')
    def index(self, **kw):
        return "Hello, world"
#
    @http.route('/demoapi/list', auth='user', csrf=False)
    def list(self, **kw):
        contacts = http.request.env['res.partner'].search([])
        result = []
        for record in contacts:
            contact = {}
            contact["id"] = record.id
            contact["name"] = record.name
            contact["phone"] = record.phone
            contact["mobile"] = record.mobile
            contact["email"] = record.email
            result.append(contact)

        return json.dumps(result)