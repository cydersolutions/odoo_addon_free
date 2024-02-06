# -*- coding: utf-8 -*-
{
    'name': 'Car Pool',
    'version': '1.0.0',
    'category': 'Business',
    'author': 'Cyder Solutions',
    'website': 'https://www.cyder.com.au/',
    'price': '3000.0',
    'currency': 'USD',
    'sequence': -100,
    'summary': 'Cs_car_pool',
    'description': """
    Cs_car_pool Program
    """,
    'depends': ['mail','hr'],
    'data': [
        'security/cs_car_pool_groups.xml',
        'security/ir.model.access.csv',
        'data/cs_car_pool_sequence.xml',
        #'reports/report.xml',
        #'reports/cs_car_pool_report.xml',
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
    'license': 'OPL-1'
}
