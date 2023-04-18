{
    'name': 'Elbaan Theme',
    'version': '16.0.1.0',
    'category': 'Theme/Creative',
    'depends': ['base', 'web','vw_main_theme_backend'],
    'author': 'ViraWeb123',
    'company': 'ViraWeb123',
    'website': 'https://viraweb123.ir',
    'description': "Elbaan Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            'elbaan_theme_backend/static/src/scss/fonts.scss',
            'elbaan_theme_backend/static/src/scss/theme.scss',
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               'elbaan_theme_backend/static/src/scss/variables.scss',
            ),
        ],
    },
}
