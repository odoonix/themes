{
    'name': 'Trip2Persia Theme',
    'version': '16.0.1.0',
    'category': 'Themes/viraWeb123',
    'depends': ['base', 'web','vw_main_theme_backend'],
    'author': 'ViraWeb123',
    'company': 'ViraWeb123',
    'website': 'https://viraweb123.ir',
    'description': "Trip2Persia Theme",
    'data': [
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            'trip2persia_theme_backend/static/src/scss/fonts.scss',
            'trip2persia_theme_backend/static/src/scss/theme.scss',
            (
               'before',
               'web/static/src/scss/primary_variables.scss',
               'trip2persia_theme_backend/static/src/scss/variables.scss',
            ),
        ],
    },
}
