# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in accounts_report/__init__.py
from accounts_report import __version__ as version

setup(
	name='accounts_report',
	version=version,
	description='Accounts Report',
	author='Dany Robert',
	author_email='rtdany10@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
