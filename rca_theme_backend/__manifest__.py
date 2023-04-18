{
    'name': 'RCAir Theme',
    'version': '16.0.1.0',
    'category': 'Themes',
    'depends': ['base', 'web','vw_main_theme_backend'],
    'author': 'ViraWeb123',
    'company': 'ViraWeb123',
    'website': 'https://viraweb123.ir',
    'description': "RCAir Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            'rca_theme_backend/static/src/scss/fonts.scss',
            'rca_theme_backend/static/src/scss/theme.scss',
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               'rca_theme_backend/static/src/scss/variables.scss',
            ),
        ],
    },
}
