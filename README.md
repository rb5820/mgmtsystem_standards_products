# Management System Standards Products

## Overview

The Management System Standards Products module enhances Odoo's product management capabilities by integrating management system standards with product data. This module allows organizations to associate industry standards, certifications, and compliance frameworks with their products.

## Features

- Link products with management system standards (ISO, IEC, NIST, etc.)
- Track product compliance with various standards
- Associate standard domains and controls with products
- Generate compliance reports for products
- Filter and search products by standard compliance

## Installation

### Prerequisites

This module requires the following dependencies:
- base
- product
- mgmtsystem
- mgmtsystem_standards

### Install Steps

1. Place the module in your Odoo addons directory
2. Update your apps list in Odoo
3. Find and install "Management System Standards Products" in the Apps menu
4. Configure access rights as needed

## Configuration

After installation:

1. Go to Settings → Users & Companies → Users
2. Assign appropriate access rights for the new functionality
3. Navigate to Management System → Configuration → Standards
4. Define the standards that will be available for products

## Usage

### Associating Standards with Products

1. Navigate to Inventory → Products
2. Select a product or create a new one
3. In the product form, navigate to the "Standards & Compliance" tab
4. Add applicable standards, domains, or controls

### Managing Product Compliance

1. Go to Management System → Products
2. Use the filters to find products by standard compliance
3. Review product compliance status
4. Generate compliance reports as needed

## Technical Information

### Models

- `mgmtsystem.standard.product`: Links products with standards and manages the compliance relationship

### Views

- Product form extension with standards management
- Standards list with product associations
- Product compliance reporting

## Troubleshooting

Common issues:
- If standards don't appear in product forms, verify that standards have been properly configured
- For access issues, check that users have the appropriate access rights assigned

## Support and Development

Developed and maintained by RB5820.

For support or enhancement requests, please contact: support@attiesatelier.be

## License

This module is licensed under LGPL-3.

---

© 2025 RB5820 - https://www.attiesatelier.be
