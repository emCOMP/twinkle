# Largely borrowed from Jeff Knupp's excellent article
# http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
#
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import io
import os
import sys

import twinkle

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

#long_description = read('README.txt', 'CHANGES.txt')


class Tox(TestCommand):
    user_optinos = []
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None    
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

class PyTest(TestCommand):
    user_options = []
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='twinkle',
    version=twinkle.__version__,
    license='MIT',
    author='emComp Lab',
    tests_require=['pytest'],
    install_requires=['pymongo>=2.7',
                    'simplejson>=3.6.2',
                    ],
    cmdclass={'test': PyTest},
    author_email='emcomp@uw.edu',
    description='Twinkle - Twitter Analysis Toolkit',
#    long_description=long_description,
    packages=['twinkle'],
    package_dir={'twinkle': 'twinkle'},
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ],
    url = 'https://github.com/emCOMP/twinkle',
    download_url = 'https://github.com/emCOMP/twinkle/tarball/' + twinkle.__version__, 
    test_suite='tests'
)

