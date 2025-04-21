# -*- coding: utf-8 -*-
{
    'name': "modulogfb",

   'summary': """
        Modulo realizado por Guillermo Fuentes Buenosvinos SGE 24-25""",
    'description': """
         Mi primer módulo en Odoo 16 \n
        ✅ Features:\n
        👉 Fácil\n
        👉 Sencillo \n
        👉 Intuitivo \n
    """,
    'author': "Guillermo Fuentes Buenosvinos",
    'website': "http://www.yourcompany.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
       
        'security/ir.model.access.csv',
        'views/menus.xml',
         'views/biblioteca_views.xml',  
    'views/autor_views.xml',      
    'views/libro_views.xml',      
            'data/data.xml',

    ],
   
     'installable': True,
}