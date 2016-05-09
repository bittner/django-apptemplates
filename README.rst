====================================
Django apptemplates |latest-version|
====================================

|python-support| |downloads| |license|

django-apptemplates is a Django template loader that allows you to load a
template from a specific application.  By this you can both extend and
override a template at the same time.  The default Django loaders require
you to copy the entire template you want to override, even if you only
want to override one small block.

Based on: http://djangosnippets.org/snippets/1376/


.. |latest-version| image:: https://img.shields.io/pypi/v/django-apptemplates.svg
   :alt: Latest version on PyPI
   :target: https://pypi.python.org/pypi/django-apptemplates
.. |python-support| image:: https://img.shields.io/pypi/pyversions/django-apptemplates.svg
   :target: https://pypi.python.org/pypi/django-apptemplates
   :alt: Python versions
.. |downloads| image:: https://img.shields.io/pypi/dm/django-apptemplates.svg
   :alt: Monthly downloads from PyPI
   :target: https://pypi.python.org/pypi/django-apptemplates
.. |license| image:: https://img.shields.io/pypi/l/django-apptemplates.svg
   :alt: Software license
   :target: https://bitbucket.org/bittner/django-apptemplates/src/default/LICENSE.txt

Version Support
===============

Python 2.4 through 3.5, and Django 1.3 through 1.9 are supported (confirmed by
primitive tests).

Installation, Setup and Use
===========================

This package is available from PyPI_.  To install it simply execute:

.. code-block:: bash

    $ pip install django-apptemplates


.. _PyPI: https://pypi.python.org/pypi/django-apptemplates

Settings (for Django 1.8+)
--------------------------

.. code-block:: python

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

.. code-block:: python

    TEMPLATE_LOADERS = (
        'apptemplates.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

How To Use In Templates
-----------------------

Template usage example (extend and override Django admin base template):

.. code-block:: python

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

1.1.1
-----

* Fix ``ImportError`` for Django 1.8 (broken in release 1.1)
* Add integration tests (test import of package across supported versions)
* Add ``clean`` and ``test`` commands to ``setup.py``

1.1
---

* Use ``django.template.Origin`` in computation of template location for Django
  1.9 compatibility. -- Thanks, `Gilles Crettenand <https://bitbucket.org/krtek/>`_!

1.0
---

* Remove Django 1.9 deprecation warning of imports
* Update README with instructions for Django 1.8+

0.2
---

*Skipped to fix conflicting versioning in setup.py and the PyPI package*

0.0.1
-----

* Released as originally published on djangosnippets
