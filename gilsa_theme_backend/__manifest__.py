{
    'name': 'gilsa Theme',
    'version': '16.0.1.0',
    'category': 'Themes',
    'depends': ['base', 'web'],
    'author': '',
    'description': "gilsa Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            '/gilsa_theme_backend/static/src/scss/fonts.scss',
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               '/gilsa_theme_backend/static/src/scss/variables.scss',
            ),
        ],
    },
}
