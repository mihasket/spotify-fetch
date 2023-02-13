#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='spotify-fetch',
    version='1.0.0',
    description='Neofetch-like tool for fetching spotify artist and album information',
    author='Miha Šket',
    url='https://github.com/mihasket/spotify-fetch',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'spotify-fetch = src.main:main',
        ]
    },
)