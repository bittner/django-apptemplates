===================
Django apptemplates
===================

django-apptemplates is a Django template loader that allows you to load a
template from a specific application.  By this you can both extend and
override a template at the same time.  The default Django loaders require
you to copy the entire template you want to override, even if you only
want to override one small block.

Based on: http://djangosnippets.org/snippets/1376/

Installation, Setup and Use
===========================

This package is available from PyPI_.  To install it simply execute: ::

    $ pip install django-apptemplates

.. _PyPI: https://pypi.python.org/pypi/django-apptemplates

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

How To Use In Templates
-----------------------

Template usage example (extend and override Django admin base template)::

    {% extends "admin:admin/base.html" %}

The part before the colon (``:``) is called the Django app *namespace*.

Alternatives
============

* django-app-namespace-template-loader_ (supports empty namespaces)

.. _django-app-namespace-template-loader: https://pypi.python.org/pypi/django-app-namespace-template-loader

Authors and Maintainers
=======================

* `Peter Bittner <https://bitbucket.org/bittner/>`_ (current maintainer)
* `Tomas Zulberti <https://bitbucket.org/tzulberti/>`_ (former maintainer)
* `Konrad Wojas <https://bitbucket.org/wojas/>`_ (original author)

Change Log
==========

0.0.1
-----

* Released as originally published on djangosnippets

0.2
---

*Skipped to fix conflicting versioning in setup.py and the PyPI package*

0.3
---

* Remove Django 1.9 deprecation warning of imports
* Update README with instructions for Django 1.8+
