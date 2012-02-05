from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='django-apptemplates',
      version=version,
      description="Django template loader that allows you to load template from a specific application",
      long_description="""\
Django template loader that allows you to load a template from a
specific application. This allows you to both extend and override
a template at the same time. The default Django loaders require you
to copy the entire template you want to override, even if you only
want to override one small block.
""",
      classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django templates',
      author='Konrad Wojas',
      author_email='konrad.wojas@jibecompany.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      """,
      )
