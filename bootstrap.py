import os
from subprocess import check_output
from sys import stderr
from ConfigParser import SafeConfigParser


class BuildConfigParser(SafeConfigParser):
	"""
	Override for implement dict representation
	"""

	def as_dict(self):
		return dict(self._sections)


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
		pkg = getattr(self, '_packages', {})
		return {k: v.split('\n') for k, v in dict(pkg).iteritems()}

	@property
	def parts(self):
		parts = getattr(self, '_parts', {})
		return {k: v for k, v in dict(parts).iteritems() if k != "__name__"}

	@property
	def extra(self):
		extra = {attr: dict(value) for attr, value in self.__dict__.iteritems() if
				 attr not in ["_env", "_packages", "_parts"]}
		print extra
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
		default_dirs = config.extra['_dirs']['default'].split(',')
		return [
			BuildCommand(config.parts['wget'], env_url),
			BuildCommand(config.parts['tar'], config.env.get('version', 'virtualenv-12.0.7')+'.tar.gz', 'xzfv'),
			BuildCommand(config.parts['python'], '.', 'virtualenv-12.0.7/virtualenv.py'),
			BuildCommand(config.parts['rm'], 'virtualenv-12.0.7 virtualenv-12.0.7.tar.gz', '-rf'),
			BuildCommand(config.parts['mkdir'], ' '.join(default_dirs), '-p')
		]

	def _parse_config(self):
		config_parser = BuildConfigParser()
		config_parser.read(self.RECIPES + 'build_env.cfg')
		config = EnvConfig(config_parser.as_dict())
		return config

	def validate(self):
		print "Validation pass \n"
		print "Check config :"
		cf = open(self.RECIPES + 'build_env.cfg')
		conf_file = cf.readlines()
		for l in conf_file:
			print l

	def rebuild(self):
		raise NotImplementedError

	def build(self):
		self.validate()
		config = self._parse_config()
		command_list = self._make_build_commands(config)
		print "Build steps:"
		for cmd in command_list:
			print cmd
		print '\n'
		print 'Starting : \n'
		for cmd in command_list:
			cmd.execute()

	def install_requirements(self):
		config = self._parse_config()
		pip = "bin/pip"
		package_list = config.packages
		print "Install commons:\n"
		for pkg in package_list['commons']:
			cmd = BuildCommand(pip, pkg, 'install')
			cmd.execute()

		print "Install frameworks:\n"
		for pkg in package_list['framework']:
			cmd = BuildCommand(pip, pkg, 'install')
			cmd.execute()

		print "Install develop:\n"
		for pkg in package_list['develop']:
			print pkg
			cmd = BuildCommand(pip, pkg, 'install', working_dir=os.environ.get('NODE_ROOT'))
			cmd.execute()

if __name__ == '__main__':
	builder = StackEnvBuilder()
	builder.build()
	builder.install_requirements()
	# parser = ArgumentParser()
	# parser.add_argument('-B', '--build', help='echo the string you use here')
	# parser.add_argument('-U', '--update', help='echo the string you use here')
	# parser.add_argument('-I', '--install', help='echo the string you use here')
	# args = parser.parse_args()
	#
	# if args.build:
	# 	builder.build()
	# elif args.install:
	# 	builder.install_requirements()