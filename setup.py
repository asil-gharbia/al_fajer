from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in al_fajer/__init__.py
from al_fajer import __version__ as version

setup(
	name="al_fajer",
	version=version,
	description="custom app ",
	author="Asil Gharbia",
	author_email="aseel.gharbia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
