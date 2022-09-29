{
    'name': 'Odoo Academy',
    'sumary': """Academy app to manage Training""",
    'description': """
        Academy Moule to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'Rude Coding',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/academy_demo.xml'
    ],
    'license': 'LGPL-3'
}