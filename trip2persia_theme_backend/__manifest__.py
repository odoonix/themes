
{
    'name': 'Trip2Persia Backend Theme', 
    'summary': 'Odoo Community Backend Theme',
    'version': '16.0.1.0.6', 
    'category': 'Themes/Backend', 
    'license': 'LGPL-3', 
    'author': 'MuK IT',
    'website': 'http://viraweb123.ir',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'base_setup',
        'web_editor',
        'mail',
    ],
    'excludes': [
        'web_enterprise',
    ],
    'data': [
        'templates/webclient.xml',
        'views/res_config_settings.xml',
        'views/res_users.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            (
                'after', 
                'web/static/src/scss/primary_variables.scss', 
                'trip2persia_theme_backend/static/src/colors.scss'
            ),
        ],
        'web._assets_backend_helpers': [
            'trip2persia_theme_backend/static/src/variables.scss',
            'trip2persia_theme_backend/static/src/mixins.scss',
        ],
        'web.assets_backend': [
            'trip2persia_theme_backend/static/src/core/**/*.xml',
            'trip2persia_theme_backend/static/src/core/**/*.scss',
            'trip2persia_theme_backend/static/src/core/**/*.js',
            'trip2persia_theme_backend/static/src/webclient/**/*.xml',
            'trip2persia_theme_backend/static/src/webclient/**/*.scss',
            'trip2persia_theme_backend/static/src/webclient/**/*.js',
            'trip2persia_theme_backend/static/src/views/**/*.scss',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': '_uninstall_cleanup',
}
