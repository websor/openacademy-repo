# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """Manage Training""",
        
    'description': """
    Open Academy module for managin trainings
    - Training COurses
    - Training sessions
    - Attendes Registration
    """,

    'author': "Alfredo E Morales P - Stellar Wholesale Inc",
    'website': "http://www.stellarinc.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/demoProfessor.xml',
    ],
}
