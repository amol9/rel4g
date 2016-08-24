import ez_setup
ez_setup.use_setuptools()

import platform
from setuptools import setup, find_packages

from rel4g.version import __version__


entry_points = {}
entry_points['console_scripts'] = ['rel4g=rel4g.main:main']
#if platform.system() == 'Windows':
#	entry_points['gui_scripts'] = ['rel4gs=rel4g.main:main']	# for use from Windows Scheduler

setup(	
	name			= 'rel4g',
	version			= __version__,
	description		= 'A command line utility to access and monitor Reliance 4G Wi-Pod.',
	author			= 'Amol Umrale',
	author_email 		= 'babaiscool@gmail.com',
	url			= 'http://pypi.python.org/pypi/rel4g/',
	packages		= ['rel4g'], 
	include_package_data	= True,
	scripts			= ['ez_setup.py'],
	entry_points 		= entry_points,
	install_requires	= ['redlib>=1.1.0', 'redcmd>=1.1.3', 'six'],
	classifiers		= [
					'Development Status :: 4 - Beta',
					'Environment :: Console',
					'License :: OSI Approved :: MIT License',
					'Natural Language :: English',
					'Operating System :: POSIX :: Linux',
					'Programming Language :: Python :: 2.7',
					'Programming Language :: Python :: 3.4',
					'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
				]
)

