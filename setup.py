# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in case_management/__init__.py
from case_management import __version__ as version

setup(
	name='case_management',
	version=version,
	description='App to manage cases.',
	author='Akram Mutaher',
	author_email='a.mutaher@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
