def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	deprecated_args = {}
	for option in self.spec_helper.iterate_option_specs():
		if option.deprecated_in_favor_of:
			deprecated_args[option.name] = option.deprecated_in_favor_of
	return deprecated_args