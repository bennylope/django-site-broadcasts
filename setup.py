#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
import broadcasts


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    author="Ben Lopatin",
    author_email="ben@benlopatin.com",
    name='django-site-broadcasts',
    version=broadcasts.__version__,
    description='A small Django app that displays temporary, '
                'short broadcasts across a site.',
    long_description=readme + '\n\n' + history,
    url='https://github.com/bennylope/django-site-broadcasts/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=1.8',
    ],
    packages=find_packages(),
    zip_safe=False,
)
