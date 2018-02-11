#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='Shuang_Tutorial',
    version='0.0.0',
    description='From zero to hero in machine learning and data science',
    author='Shuang Li',
    author_email='shuang.li@bcm.edu',
    url='https://github.com/ShuangLiBCM/Shuang_Tutorial',
    packages=find_packages(exclude=[]),
    install_requires=['numpy'],
)