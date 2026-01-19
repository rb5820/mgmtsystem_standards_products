# -*- coding: utf-8 -*-
{
    'name': '🛡️ Management System Standards - Products Integration',
    'version': '18.0.0.0.1',
    'summary': '🎯 Link Products with Management System Standards for Compliance Tracking',
    'description': """
========================================
🛡️ Management System Standards Products v18.0.0.0.1
========================================

This module provides comprehensive integration between product management and management system standards compliance tracking for enterprise quality management.

🆕 Key Features:
- 📊 **Product-Standard Mapping**: Link products directly to applicable management system standards
- 🏷️ **Multi-Standard Support**: Support for ISO 27001, ISO 9001, and other management system standards
- 📋 **Compliance Tracking**: Track which products comply with specific standards
- 🔗 **Hierarchical Structure**: Parent-child relationships for complex product structures
- 📈 **Reporting & Analytics**: Generate compliance reports and track standard coverage
- 🏢 **Multi-Company Ready**: Full support for multi-company environments
- 📧 **Activity Tracking**: Mail integration for compliance status updates

🎯 Core Functionality:
- **Product Template Extension**: Add standards compliance directly to product forms
- **Standard Domain Products**: Manage product categories within standard domains  
- **Compliance Evidence**: Track proof of conformity and implementation evidence
- **Document Management**: Link compliance documents to product-standard relationships
- **Visual Interface**: Clean, intuitive UI with modern design elements

🔧 Technical Features:
- Full integration with Odoo's product management system
- Parent-store hierarchy support for complex product structures
- Advanced search and filtering capabilities
- Export compliance data for audits
- API-ready for external integrations

📈 Perfect for:
- Manufacturing companies requiring standards compliance
- Quality management departments
- Compliance officers and auditors
- Organizations with complex product portfolios
- Companies managing multiple management system standards

🎯 Seamless integration with the broader RB5820 management system ecosystem for complete compliance management.
""",
    'author': 'RB5820',
    'depends': ['base', 'mail', 'product', 'mgmtsystem', 'mgmtsystem_standards'],
    'category': '🛡️ Management System/Product Integration',
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
    
    # Images for the app store
    'images': [
        'static/description/icon.png',
        'static/description/banner.png',
        'static/description/screenshot_01.png',
        'static/description/screenshot_02.png',
    ],
    
    # App configuration
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}

