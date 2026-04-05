{
    "name": "Elbaan Theme",
    "version": "17.0.1.0",
    "category": "Themes/Services",
    "depends": ["base", "web", "main_theme_backend"],
    "author": "MoonSun",
    "company": "MoonSun",
    "website": "https://www.moonsun.au",
    "description": "Elbaan Theme",
    "data": [],
    "demo": [],
    "installable": True,
    "license": "LGPL-3",
    "assets": {
        "web._assets_primary_variables": [
            "elbaan_theme_backend/static/src/scss/fonts.scss",
            "elbaan_theme_backend/static/src/scss/theme.scss",
            (
                "before",
                "web/static/src/scss/primary_variables.scss",
                "elbaan_theme_backend/static/src/scss/variables.scss",
            ),
        ],
    },
}
