# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_cloud_migrator/__init__.py
from frappe_cloud_migrator import __version__ as version

setup(
	name='frappe_cloud_migrator',
	version=version,
	description='Migrate Sites to Frappe Cloud',
	author='Frappe',
	author_email='aditya@erpnext.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
