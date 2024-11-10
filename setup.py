#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='sfetch',
    version='1.1.0',
    description='Neofetch-like tool for fetching spotify artist and album information',
    author='Miha Šket',
    url='https://github.com/mihasket/spotify-fetch',
    packages=find_packages(),
    install_requires=['spotipy', 'climage', 'python-dotenv'],
    entry_points={
        'console_scripts': [
            'sfetch = src.main:main',
        ]
    },
)
