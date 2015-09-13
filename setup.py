from os.path import dirname, join
from setuptools import setup, find_packages

version = '0.2.1'


def read(fname):
    return open(join(dirname(__file__), fname)).read()

setup(name='django-apptemplates',
      version=version,
      description='Django template loader that allows you to load and'
                  'override a template from a specific Django application.',
      long_description=read('README.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Software Development :: Libraries :: Application Frameworks',  # noqa
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='django templates',
      author='Konrad Wojas',
      author_email='konrad.wojas@jibecompany.com',
      maintainer='Tomas Zulberti',
      url='http://bitbucket.org/tzulberti/django-apptemplates/',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
)
