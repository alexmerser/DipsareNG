import os
from setuptools import setup, find_packages

__name__ = "sn_ext"
__version__ = 'dev0.0.1'

_path = os.path.abspath(os.path.dirname(__file__))
_README = unicode(open(os.path.join(_path, 'README.rst')).read(), 'utf-8')
_CHANGES = unicode(open(os.path.join(_path, 'CHANGES.rst')).read(), 'utf-8')

setup(
	name=__name__,
	version=__version__,
	author="drs",
	author_email="info@drs.systems",
	description="Extension",
	long_description=_README + '\n \n' + _CHANGES,
	license="OPEN YOLONIGASWAG",
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
)