"""
Configuration file for py.test
"""

import django


def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "test.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "broadcasts",
        ],
        MIDDLEWARE_CLASSES=[],
        SITE_ID=1,
        ROOT_URLCONF="tests.urls",
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            },
        ]
    )
    django.setup()
