#!/usr/bin/env python
from glob import glob
from os import remove
from os.path import dirname, join
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from shlex import split
from shutil import rmtree

version = '1.2.0.dev1'


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from tox import cmdline
        args = self.tox_args
        if args:
            args = split(self.tox_args)
        errno = cmdline(args=args)
        exit(errno)


class Clean(TestCommand):
    def run(self):
        delete_in_root = [
            'build',
            '.cache',
            'dist',
            '.eggs',
            '*.egg-info',
            '.tox',
        ]
        delete_everywhere = [
            '__pycache__',
            '*.pyc',
        ]
        for candidate in delete_in_root:
            rmtree_glob(candidate)
        for visible_dir in glob('[A-Za-z0-9]*'):
            for candidate in delete_everywhere:
                rmtree_glob(join(visible_dir, candidate))
                rmtree_glob(join(visible_dir, '*', candidate))
                rmtree_glob(join(visible_dir, '*', '*', candidate))


def rmtree_glob(file_glob):
    for fobj in glob(file_glob):
        try:
            rmtree(fobj)
            print('%s/ removed ...' % fobj)
        except OSError:
            try:
                remove(fobj)
                print('%s removed ...' % fobj)
            except OSError:
                pass


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
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
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
      url='http://bitbucket.org/bittner/django-apptemplates/',
      license='MIT License',
      include_package_data=True,
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      tests_require=['tox', 'virtualenv<14.0.0'],
      cmdclass={
          'clean': Clean,
          'test': Tox,
      },
      zip_safe=False)
