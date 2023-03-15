{
    'name': 'Cyder Travel Log',
    'version': '15.0.1.1.0',
    'summary': 'Extends fleet to add travel information',
    'category': 'Productivity',
    'author': 'Cyder Solutions',
    'website': 'https://www.cyder.com.au',
    'description': """
Extends fleet to add travel information
""",
    'depends': ['fleet'],
    'data': [
        'views/trips.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': -90,
}
