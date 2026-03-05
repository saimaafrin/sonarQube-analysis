def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
cannot be read due to insufficient permissions or error parsing configuration file, the error log will
be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	configs = {}
	errors = []
	for config_filename in config_filenames:
		config = {}
		try:
			with open(config_filename, 'r') as f:
				config = yaml.load(f)
		except IOError as e:
			errors.append(e)
		except yaml.YAMLError as e:
			errors.append(e)
		if config:
			configs[config_filename] = config
	if overrides:
		for k, v in overrides.items():
			configs[k] = v
	if resolve_env:
		for config in configs.values():
			resolve_env_vars(config)
	return configs, errors