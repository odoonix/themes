{
    'name': 'Ekraam Theme',
    'version': '16.0.1.0',
    'category': 'Themes',
    'depends': ['base', 'web','vw_main_theme_backend'],
    'author': 'ViraWeb123',
    'company': 'ViraWeb123',
    'website': 'https://viraweb123.ir',
    'description': "Ekraam Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            'ekraam_theme_backend/static/src/scss/fonts.scss',
            'ekraam_theme_backend/static/src/scss/theme.scss',
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               'ekraam_theme_backend/static/src/scss/variables.scss',
            ),
        ],
    },
}
