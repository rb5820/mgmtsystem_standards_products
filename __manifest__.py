# -*- coding: utf-8 -*-
{
    'name': 'Managementsystem Standards Products',
    'version': '18.0.0.0.0',
    'summary': 'Manage Management System Standards',
    'description': 'A module to manage management system standards on products',
    'author': 'RB5820',
    'depends': ['base', 'mail', 'product', 'mgmtsystem', 'mgmtsystem_standards'],
    'category': 'RB5820',
    'website': "https://www.attiesatelier.be",
    'data': [
        'security/ir.model.access.csv',
        'views/mgmtsystem_standard_product_views.xml',
        #'views/mgmtsystem_standard_views.xml',
        #'data/mgmtsystem_standard_data.xml',
    ],

    # only loaded in demonstration mode
    'demo': [

    ],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}

