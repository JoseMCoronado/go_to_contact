# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Open Child Contacts from Contact Form View',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Open child contact form view from res.partner child_ids kanban card.
        """,
    'depends': ['base'],
    'data': [
        'data/ir_views_actions.xml'
    ],
    'installable': True,
}
