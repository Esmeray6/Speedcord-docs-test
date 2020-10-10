"""
Created by Epic at 9/4/20
"""
from setuptools import setup

setup(
	name='speds',
	version="0.0.1",
	url='https://github.com/tag-epic/speedcord',
	license='MIT',
	author='me',
	long_description="yolo",
	long_description_content_type="text/markdown",
	install_requires=["aiohttp", "ujson", "sphinx", "sphinx", "sphinxcontrib_trio", "sphinxcontrib-websupport"],
	description='A simple lightweight discord library',
	python_requires='>=3.7',
)
