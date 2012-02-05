djang-apptemplates is a Django template loader that allows you to load a 
template from a specific application. This allows you to both extend and 
override a template at the same time. The default Django loaders require 
you to copy the entire template you want to override, even if you only
want to override one small block.

Template usage example (extend and override Django admin base template)::

    {% extends "admin:admin/base.html" %}

Settings::

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'apptemplates.Loader',
    )

Based on: http://djangosnippets.org/snippets/1376/
