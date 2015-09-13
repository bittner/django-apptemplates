===================
Django apptemplates
===================

django-apptemplates is a Django template loader that allows you to load a
template from a specific application.  By this you can to both extend and
override a template at the same time.  The default Django loaders require
you to copy the entire template you want to override, even if you only
want to override one small block.

Based on: http://djangosnippets.org/snippets/1376/

Usage
=====

Template usage example (extend and override Django admin base template)::

    {% extends "admin:admin/base.html" %}

The part before the colon (``:``) is the Django app namespace.

Setup
=====

Settings (for Django 1.8+)
--------------------------

::

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

Settings (for Django < 1.8)
---------------------------

::

    TEMPLATE_LOADERS = (
        'apptemplates.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

Alternatives
============

* django-app-namespace-template-loader_ (supports empty namespaces)

.. _django-app-namespace-template-loader: https://pypi.python.org/pypi/django-app-namespace-template-loader
