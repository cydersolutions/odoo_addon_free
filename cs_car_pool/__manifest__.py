# -*- coding: utf-8 -*-
{
    'name': 'Car Pool',
    'version': '1.2.2',
    'category': 'Business',
    'author': 'Cyder Solutions',
    'website': 'https://www.cyder.com.au/',
    'sequence': 10,
    'summary': 'Car Pool',
    'description': """
    Car Pool Program
    """,
    'depends': ['mail','hr'],
    'data': [
        'security/cs_car_pool_groups.xml',
        'security/ir.model.access.csv',
        'data/cs_car_pool_sequence.xml',
        'data/mail_template_data.xml',
        #'reports/report.xml',
        'reports/cs_car_pool_report.xml',
        'views/top_menu.xml',
        'views/cs_car_pool_view.xml',
        'views/cs_car_pool_vehicles_view.xml',
        'views/cs_car_pool_bookings_view.xml',
        'views/hr_employee_view.xml',
    ],
    'demo': [],
    'images': ['static/description/banner.gif'],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
