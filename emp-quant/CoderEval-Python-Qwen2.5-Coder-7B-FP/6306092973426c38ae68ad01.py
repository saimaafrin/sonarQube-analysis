def get_deprecated_args(self):
deprecated_options = {}
	for option in self.spec_helper.iterate_option_specs():
		if option.deprecates:
			deprecated_options[option.name] = option.deprecates
	return deprecated_options