====================================
Django apptemplates |latest-version|
====================================

|build-status| |python-support| |downloads| |license|

django-apptemplates is a Django template loader that allows you to load a
template from a specific application.  By this you can both extend and
override a template at the same time.  The default Django loaders require
you to copy the entire template you want to override, even if you only
want to override one small block.

Based on: http://djangosnippets.org/snippets/1376/


.. |latest-version| image:: https://img.shields.io/pypi/v/django-apptemplates.svg
   :alt: Latest version on PyPI
   :target: https://pypi.python.org/pypi/django-apptemplates
.. |build-status| image:: https://travis-ci.org/bittner/django-apptemplates.svg?branch=master
   :alt: Build status
   :target: https://travis-ci.org/bittner/django-apptemplates
.. |python-support| image:: https://img.shields.io/pypi/pyversions/django-apptemplates.svg
   :target: https://pypi.python.org/pypi/django-apptemplates
   :alt: Python versions
.. |downloads| image:: https://img.shields.io/pypi/dm/django-apptemplates.svg
   :alt: Monthly downloads from PyPI
   :target: https://pypi.python.org/pypi/django-apptemplates
.. |license| image:: https://img.shields.io/pypi/l/django-apptemplates.svg
   :alt: Software license
   :target: https://github.com/bittner/django-apptemplates/blob/master/LICENSE.txt

Version Support
===============

Python 2.6 through 3.5, and Django 1.4 and above are supported (verified by
tests).

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

How to Use in Templates
-----------------------

Template usage example (extend and override Django admin base template):

.. code-block:: python

    {% extends "admin:admin/base.html" %}

The part before the colon (``:``) is called the Django app *namespace*.

Alternatives
============

* django-app-namespace-template-loader_ (supports empty namespaces)


.. _django-app-namespace-template-loader:
    https://pypi.python.org/pypi/django-app-namespace-template-loader

Authors and Maintainers
=======================

* `Peter Bittner`_ (current maintainer)
* `Tomas Zulberti`_ (former maintainer)
* `Konrad Wojas`_ (original author)


.. _Peter Bittner: https://bitbucket.org/bittner/django-apptemplates
.. _Tomas Zulberti: https://bitbucket.org/tzulberti/django-apptemplates
.. _Konrad Wojas: https://bitbucket.org/wojas/django-apptemplates

Change Log
==========

1.2
---

* Reestablish support for Django 1.4 through 1.8 (broken since version 1.1)
* Add tests for template rendering
* Drop support for Django 1.3 (which cannot be confirmed by tests)
* Drop support for Python 2.4 and 2.5 (which cannot be tested anymore)

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
