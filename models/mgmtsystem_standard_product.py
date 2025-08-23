# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class MgmtSystemStandardProduct(models.Model):
    _name = 'mgmtsystem.standard.product'
    _description = 'Management System Standard Product'
    _parent_name = 'parent_id'                  # by default its name is parent_id you can change it
    _parent_store = True                        # tell odoo that this model support parent & child relation ship
    _check_company_auto = True

    
    parent_id = fields.Many2one('mgmtsystem.standard.product', string='Parent', index=True, ondelete='cascade')
    child_ids = fields.One2many('mgmtsystem.standard.product', 'parent_id', string='Children')
    parent_path = fields.Char(index=True)
    name = fields.Char(
        string='Product Name',
        tracking=True,
        help='Name of the product related to the management system standard'
    )

    product_id = fields.Many2one(
        'product.template',
        string='Product',
        required=True
    )


    standard_id = fields.Many2one(
        'mgmtsystem.standard',
        'Parent', 
        store=True
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

    standard_domain_id = fields.Many2one(
        'mgmtsystem.standard.domain',
        string='Standard Domain',
    )

    standard_domain_name= fields.Char(
        related='standard_domain_id.name',
        string='Standard Domain Name',
        store=True,
        readonly=True
    )
    standard_domain_version = fields.Char(
        related='standard_domain_id.version',
        string='Standard Domain Version',
        store=True,
        readonly=True
    )
    standard_domain_title = fields.Char(
        related='standard_domain_id.title',
        string='Standard Domain Title',
        store=True,
        readonly=True
    )
    standard_domain_state = fields.Selection(
        related='standard_domain_id.state',
        string='Standard Domain State',
        store=True,
        readonly=True
    )
    



    proof_of_conformity = fields.Selection(
        selection=[
            ('certified', 'Certified'),
            ('declaration', 'Declaration of Conformity'),
            ('self_assessment', 'Self-Assessment'),
            ('other', 'Other')
        ],
        string='Proof of Conformity',
        required=True
    )

    implementation_evidence = fields.Text(
        string="Implementation Evidence",
        help="Description of evidence needed to demonstrate compliance"
    )

    document_ids = fields.Many2many(
        'ir.attachment',
        string='Documents',
        help="Related documents and evidence"
    )

    # state = fields.Selection(
    #     selection_add=[
    #         ('maintenance', 'Under Maintenance'),
    #         ('decommissioned', 'Decommissioned')
    #     ],
    #     string='Status',
    #     default='draft',
    # )
    description = fields.Text(string='Description')
    product_ids = fields.Many2many('product.template', string='Products')

    
    # Multi company 
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    allowed_company_ids = fields.Many2many('res.company', string='Allowed Companies')