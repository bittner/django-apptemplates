import django
import pytest  # noqa

from copy import deepcopy
from django.conf import settings
from django.template.base import Context, Template
try:
    from django.test.utils import override_settings
except ImportError:  # older Djangos
    from django.test import override_settings


cached_template_settings = {}
if django.VERSION < (1, 8):
    cached_template_settings['TEMPLATE_LOADERS'] = [
        ('django.template.loaders.cached.Loader', settings.TEMPLATE_LOADERS)
    ]
else:
    TEMPLATES = deepcopy(settings.TEMPLATES)
    opt = TEMPLATES[0]['OPTIONS']
    opt['loaders'] = [
        ('django.template.loaders.cached.Loader', opt['loaders'])
    ]
    cached_template_settings['TEMPLATES'] = TEMPLATES


def test_import():
    """
    Importing this module should not fail.
    """
    import apptemplates
    assert apptemplates.__name__ == 'apptemplates'


def test_render():
    """
    Test-drive the apptemplate code base by rendering a template.
    """
    c = Context()
    t = Template('{% extends "admin:admin/base.html" %}')
    t.render(c)


@override_settings(**cached_template_settings)
def test_cached():
    """
    Test that the template still works when the cached loader is being used.
    """
    c = Context()
    t = Template('{% extends "admin:admin/base.html" %}')
    t.render(c)
