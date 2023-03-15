{
    'name': 'Cyder Travel Log',
    'version': '15.0.1.1.0',
    'summary': 'Extends fleet to add travel information',
    'author': 'Cyder Solutions',
    'category': 'Productivity',
    'description': """
Extends fleet to add travel information
""",
    'website': 'https://www.cyder.com.au',
    'depends': ['fleet'],
    'data': [
        'views/trips.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': -101,
}
