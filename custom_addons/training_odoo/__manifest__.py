# # -*- coding: utf-8 -*-
# {
#     'name': "training_odoo",

#     'summary': "Short (1 phrase/line) summary of the module's purpose",

#     'description': """
# Long description of module's purpose
#     """,

#     'author': "My Company",
#     'website': "https://www.yourcompany.com",

#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',

#     # any module necessary for this one to work correctly
#     'depends': ['base'],

#     # always loaded
#     'data': [
#         # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
# }


# -*- coding: utf-8 -*-
{
    'name': "Training Odoo",
 
    'summary': " Modul untuk latihan teknikal Odoo. ",
 
    'description': """ 
        Modul ini berfungsi untuk mempraktekan teknikal documentation pada website resmi odoo.com. 
        Sebagian hal yang akan dipelajari adalah :
        - ORM
        - Berbagai View
        - Report
        - Wizard
        - Dll 
    """,
 
    'author': "PPM Manajemen",
 
    'website': "ppm-manajemen.ac.id",
 
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
 
    'version': '0.1',
 
    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mail'],
 
    # always loaded
    'data': [
        'report/report_training_session.xml',
        'report/report_action.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sequence_data.xml',
        'views/scheduler_data.xml',
        'views/views.xml',
        'views/partner_views.xml',
        'wizard/training_wizard_views.xml',
        'views/menuitem_views.xml',
        'views/templates.xml',
],
     
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

