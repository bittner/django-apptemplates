"""Django settings for testing django-apptemplates"""
import django

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
)

ROOT_URLCONF = 'apptemplates.test.urls'

SECRET_KEY = 'secret-key'

if django.VERSION[:2] < (1, 8):
    TEMPLATE_LOADERS = (
        'apptemplates.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'loaders': [
                    'apptemplates.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]
