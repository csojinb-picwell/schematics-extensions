#!/usr/bin/env python

from distutils.core import setup

requirements = [
    'schematics==1.0-0',
]

setup(name='schematics-extensions',
      version='1.0',
      description='Picwell Commercial library',
      author='Picwell',
      author_email='dev@picwell.com',
      url='http://www.picwell.com/',
      install_requires=requirements)
