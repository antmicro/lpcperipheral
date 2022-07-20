#!/usr/bin/env python

from setuptools import setup

setup(
    name='lpcperipheral',
    version='1.0',
    author='IBM Corp.',
    description='LPC peripheral that implements LPC IO and FW cycles',
    url='https://github.com/OpenPOWERFoundation/lpcperipheral',
    license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
    install_requires=[
        'amaranth',
        'amaranth-soc@git+https://github.com/amaranth-lang/amaranth-soc.git'
    ],
)
