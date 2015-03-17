import os
from setuptools import setup, find_packages

__name__ = "sn_core"

_path = os.path.abspath(os.path.dirname(__file__))
_README = unicode(open(os.path.join(_path, 'README.rst')).read(), 'utf-8')
_CHANGES = unicode(open(os.path.join(_path, 'CHANGES.rst')).read(), 'utf-8')

setup(
	name=__name__,
	version='dev0',
	author="drs",
	author_email="info@drs.systems",
	description="Core",
	long_description=_README + '\n \n' + _CHANGES,
	license="OPEN YOLONIGASWAG",
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	entry_points='''
		[console_scripts]
		core/run=sn_core.run_core:main
	'''
)