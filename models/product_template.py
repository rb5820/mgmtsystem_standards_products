# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    standard_ids = fields.Many2many(
        'mgmtsystem.standard',
        'product_template_standard_rel',
        'product_tmpl_id',
        'standard_id',
        string='Standards'
    )

    standard_id = fields.Many2one(
        'mgmtsystem.standard',
        string='Standard',
        required=False
    )

    standard_name = fields.Char(
        related='standard_id.name',
        string='Standard Name',
        store=True,
        readonly=True
    )


    standard_version = fields.Char(
        related='standard_id.version',
        string='Version',
        store=True,
        readonly=True
    )

    standard_title = fields.Char(
        related='standard_id.title',
        string='Standard Title',
        store=True,
        readonly=True
    )

    standard_state = fields.Selection(
        related='standard_id.state',
        string='Standard State',
        store=True,
        readonly=True
    )

    mgmtsystem_standard_product_ids = fields.One2many(
    'mgmtsystem.standard.product',
    'product_id',
    string='Management System Standards'
    )


    product_standard_domain_ids = fields.One2many(
        'mgmtsystem.standard.domain.product',
        'product_id',
        string='Standard Domain Products'
    )



    standard_domain_id = fields.Many2one(
        'mgmtsystem.standard.domain',
        string='Standard Domain',
        required=False
    )


    product_standard_domain_name= fields.Char(
        related='standard_domain_id.name',
        string='Standard Domain Name',
        store=True,
        readonly=True
    )

    # Note: 'product_standard_domain_version' is not included here as it
    # is not defined in the 'mgmtsystem.standard.domain.product' model.
    # If needed, it can be added similarly to 'product_standard_domain_name'.

    # product_standard_domain_version = fields.Char(
    #     related='product_standard_domain_ids.version',
    #     string='Standard Domain Version',
    #     store=True,
    #     readonly=True
    # )

    product_standard_domain_title = fields.Char(
        related='standard_domain_id.title',
        string='Standard Domain Title',
        store=True,
        readonly=True
    )
    product_standard_domain_state = fields.Selection(
        related='standard_domain_id.state',
        string='Standard Domain State',
        store=True,
        readonly=True
    )

    # multi company
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)