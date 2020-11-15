# -*- coding: utf-8 -*-
{
    'name': "Costa Rica - Zones for Electronic Invoices",

    'summary': """Costa Rica - Zones for Electronic Invoices.""",

    'description': """
        Costa Rica - Zones for Electronic Invoices.
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '13.0.0.4',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_country_canton.xml',
        'views/res_country_distrito.xml',
        'views/res_country_barrio.xml',
        'views/access_views.xml',
        'views/res_partner.xml',
        'data/res.country.canton.csv',
        'data/res.country.distrito.csv',
        'data/res.country.barrio.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
