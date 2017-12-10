#!/usr/bin/env python
from os.path import dirname, join
from setuptools import setup, find_packages

version = '1.4'


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(name='django-apptemplates',
      version=version,
      description='Django template loader that allows you to load and '
                  'override a template from a specific Django application.',
      long_description=read_file('README.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.4',
          'Framework :: Django :: 1.5',
          'Framework :: Django :: 1.6',
          'Framework :: Django :: 1.7',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Framework :: Django :: 1.10',
          'Framework :: Django :: 1.11',
          'Framework :: Django :: 2.0',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Software Development :: Libraries :: Application Frameworks',  # noqa
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords=['django', 'template', 'loader'],
      author='Konrad Wojas',
      author_email='bitbucket@m.wojas.nl',
      maintainer='Peter Bittner',
      maintainer_email='django@bittner.it',
      url='https://github.com/bittner/django-apptemplates',
      license='MIT',
      include_package_data=True,
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      tests_require=['tox', 'virtualenv<14.0.0'],
      zip_safe=False)
