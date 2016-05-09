import pytest  # noqa


def test_import():
    import apptemplates
    assert apptemplates.__name__ == 'apptemplates'
