====================================
Django apptemplates |latest-version|
====================================

|build-status| |health| |python-support| |license|

django-apptemplates is a Django template loader that allows you to load a
template from a specific application.  By this you can both extend and
override a template at the same time.  The default Django loaders require
you to copy the entire template you want to override, even if you only
want to override one small block.

Based on: http://djangosnippets.org/snippets/1376/


.. |latest-version| image:: https://img.shields.io/pypi/v/django-apptemplates.svg
   :alt: Latest version on PyPI
   :target: https://pypi.python.org/pypi/django-apptemplates
.. |build-status| image:: https://img.shields.io/travis/bittner/django-apptemplates/master.svg
   :alt: Build status
   :target: https://travis-ci.org/bittner/django-apptemplates
.. |health| image:: https://img.shields.io/codacy/grade/a9be2f4c385545e381c3a317f52782c5/master.svg
   :target: https://www.codacy.com/app/bittner/django-apptemplates
   :alt: Code health
.. |python-support| image:: https://img.shields.io/pypi/pyversions/django-apptemplates.svg
   :target: https://pypi.python.org/pypi/django-apptemplates
   :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/django-apptemplates.svg
   :alt: Software license
   :target: https://github.com/bittner/django-apptemplates/blob/master/LICENSE.txt

Version Support
===============

django-apptemplates is `tested against`_ the officially supported combinations
of Python and Django, since Django 1.4 (Django 1.4 to 3.0 on Python 2.7, and
3.4 to 3.8).


.. _tested against: https://travis-ci.org/bittner/django-apptemplates

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

1.5
---

* Drop support for Django 1.7 (ImportError)
* Drop support for Python 2.6, 3.2, 3.3 (not available on Travis CI)

1.4
---

* Fix Origin missing loader and template_name attrs -- Thanks Brendan Roy,
  @bmon, and Matthew Somerville, @dracos!
* Also test against Django 2.0

1.3
---

* Add template loader to returned Origins -- Thanks J.J., @jdotjdot!
* Also test against Python 3.6 -- Thanks Justin Walgran, @jwalgran!

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
