# -*- coding: utf-8 -*-
{
    'name': '🛡️ Management System Standards - Products Integration',
    'version': '18.0.0.0.1',
    'summary': '🎯 Link Products with Management System Standards for Compliance Tracking',
    'description': """
Link products with management system standards for comprehensive compliance tracking.

Features: Product-standard mapping, compliance tracking, hierarchical structures, 
reporting & analytics, multi-company support, and document management.

Perfect for manufacturing companies, quality departments, and compliance officers.
""",
    'author': 'RB5820',
    'depends': ['base', 'mail', 'product', 'mgmtsystem', 'mgmtsystem_standards'],
    'category': 'RB5820/Product Integration',
    'website': "https://www.attiesatelier.be",
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Views
        'views/mgmtsystem_standard_product_views.xml',
        #'views/mgmtsystem_standard_views.xml',
        
        # Data
        #'data/mgmtsystem_standard_data.xml',
    ],

    # Demo data (only loaded in demonstration mode)
    'demo': [
        # Add demo data files here if needed
    ],
    
    # App configuration
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

