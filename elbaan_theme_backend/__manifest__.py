{
    'name': 'Elbaan Theme',
    'version': '16.0.1.0',
    'category': 'Themes',
    'depends': ['base', 'web'],
    'author': '',
    'description': "Elbaan Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               '/elbaan_theme_backend/static/src/scss/variables.scss',
            ),
        ],
        'web.assets_backend': [
            '/elbaan_theme_backend/static/src/scss/fonts.scss',
        ],
    },
}
