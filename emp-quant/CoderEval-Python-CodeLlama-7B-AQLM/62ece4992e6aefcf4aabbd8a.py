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
		config = load_configuration(config_filename, overrides, resolve_env)
		if config is None:
			errors.append(logging.LogRecord(logging.ERROR, logging.ERROR, config_filename, 0, "Unable to read configuration file", None, None))
		else:
			configs[config_filename] = config
	return configs, errors