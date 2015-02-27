try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twinkle - Twitter Network Analysis',
    'author': 'emCOMP Lab',
    'url': 'https://depts.washington.edu/emcomp/',
    'download_url': 'Where to download it.',
    'author_email': 'emcomp@uw.edu',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['twinkle'],
    'scripts': [],
    'name': 'twinkle'
}

setup(**config)