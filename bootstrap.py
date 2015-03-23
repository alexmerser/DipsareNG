import os
from sys import stderr
import json
from subprocess import check_output


class BuildCommand():
	def __init__(self, part, args, options=None, echo=True, working_dir=None):
		self._part = part
		self._options = options
		self._echo = echo
		self._working_dir = working_dir
		self._local_args = args

	def _compose(self):
		return '{0} {1} {2}'.format(self._part, self._options, self._local_args) if self._options \
			else '{0} {1}'.format(self._part, self._local_args)

	def _validate(self):
		raise NotImplementedError

	def execute(self):
		"""
		Run 'command' in the shell and return its standard out.
		:return: command output
		"""
		if self._echo:
			print '[builder] >> cmd:{0} | options: {1} | args: {2}'.format(self._part, self._options, self._local_args)
		out = check_output(self._compose(), stderr=stderr, shell=True, cwd=self._working_dir)
		if self._echo:
			print out
		return out

	def __repr__(self):
		return "<BuildCommand {}>".format(self._compose())


class EnvConfig(object):
	"""
	Domain level representation config from config parser.
	"""

	def __init__(self, config_dict):
		for arg, value in config_dict.iteritems():
			setattr(self, '_%s' % arg, value)

	def __repr__(self):
		env = self.env
		vers = 'undefined'
		if env:
			vers = env['version']
		return "<BuildConfig %s>" % vers

	@property
	def env(self):
		env = getattr(self, '_env', {})
		return dict(env)

	@property
	def packages(self):
		return getattr(self, '_packages', {})

	@property
	def parts(self):
		parts = getattr(self, '_parts', {})
		return {k: v for k, v in dict(parts).iteritems() if k != "__name__"}

	@property
	def extra(self):
		extra = {
			attribute: value for attribute, value in self.__dict__.iteritems() if
			attribute not in ["_env", "_packages", "_parts"]
		}
		return extra


class StackEnvBuilder(object):

	RECIPES = os.path.abspath(os.path.dirname(__file__)) + '/recipes/'

	@staticmethod
	def _make_build_commands(config):
		env = config.env
		env_url = '{0}{1}{2}'.format(
			env.get('env_url', 'http://pypi.python.org/packages/source/v/virtualenv/'),
			env.get('version', 'virtualenv-12.0.7'),
			env.get('dist_ext', '.tar.gz')
		)
		default_dirs = config.extra['_dirs']['default']
		return [
			BuildCommand(config.parts['wget'], env_url),
			BuildCommand(config.parts['tar'], config.env.get('version', 'virtualenv-12.0.7')+'.tar.gz', 'xzfv'),
			BuildCommand(config.parts['python'], '.', 'virtualenv-12.0.7/virtualenv.py'),
			BuildCommand(config.parts['rm'], 'virtualenv-12.0.7 virtualenv-12.0.7.tar.gz', '-rf'),
			BuildCommand(config.parts['mkdir'], ' '.join(default_dirs), '-p')
		]

	def _parse_config(self):
		cfg = json.load(file(self.RECIPES + 'build_config.json'))
		config = EnvConfig(cfg)
		return config

	def validate(self):
		print "Validation \n"
		json.load(file(self.RECIPES + 'build_config.json'))

	def rebuild(self):
		raise NotImplementedError

	def build(self):
		self.validate()
		config = self._parse_config()
		command_list = self._make_build_commands(config)
		for cmd in command_list:
			cmd.execute()

	@staticmethod
	def _installed_pkg():
		pip = "bin/pip"
		cmd = BuildCommand(pip, 'freeze')
		pkg_list = cmd.execute()
		return str(pkg_list).split('\n')[:-1]

	@staticmethod
	def _upgradable(pkg, check):
		installed = {}
		for item in check:
			splited = item.split("==")
			if len(splited) > 1:
				p = {splited[0]: splited[1]}
				installed.update(p)
		pkg_name = pkg.split('==')[0]
		current_version = pkg.split('==')[1]

		return True if installed.get(pkg_name, None) < current_version else False

	# TODO 1: refactor this tones of ctrl-c/ctrl-v
	# TODO 2: make install/update action related on package versions
	# TODO 3: make dev/user builds related to env_id generated for particular user
	def install_requirements(self):
		config = self._parse_config()
		pip = "bin/pip"
		check_list = self._installed_pkg()
		package_list = config.packages
		to_install = []
		to_update = []

		for pkg in package_list['commons']:
			if pkg not in check_list:
				to_install.append(pkg)
			elif self._upgradable(pkg, check_list):
				to_update.append(pkg)
			else:
				continue

		for pkg in package_list['framework']:
			if pkg not in check_list:
				to_install.append(pkg)
			elif self._upgradable(pkg, check_list):
				to_update.append(pkg)
			else:
				continue

		for pkg in package_list['develop']:
			if pkg not in check_list:
				to_install.append(pkg)
			else:
				to_update.append(pkg)

		for pkg in to_install:
			cmd = BuildCommand(pip, pkg, 'install', working_dir=os.environ.get('NODE_ROOT'))
			cmd.execute()

		for pkg in to_update + to_install:
			cmd = BuildCommand(pip, pkg, 'install --upgrade', working_dir=os.environ.get('NODE_ROOT'))
			cmd.execute()

if __name__ == '__main__':
	builder = StackEnvBuilder()
	builder.build()
	builder.install_requirements()