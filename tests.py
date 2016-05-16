import pytest  # noqa
from django.template.base import Context, Template


def test_import():
    import apptemplates
    assert apptemplates.__name__ == 'apptemplates'


def test_render():
    c = Context()
    t = Template('{% extends "admin:admin/base.html" %}')
    t.render(c)
