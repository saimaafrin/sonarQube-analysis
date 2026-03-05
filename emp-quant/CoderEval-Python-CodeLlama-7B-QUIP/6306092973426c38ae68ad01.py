def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	return {
		'--deprecated': {
			'--deprecated': '--deprecated',
			'--deprecated-option': '--deprecated-option',
			'--deprecated-option-with-value': '--deprecated-option-with-value',
			'--deprecated-option-with-value-and-default': '--deprecated-option-with-value-and-default',
			'--deprecated-option-with-value-and-default-and-default': '--deprecated-option-with-value-and-default-and-default',
			'--deprecated-option-with-value-and-default-and-default-and-default': '--deprecated-option-with-value-and-default-and-default-and-default',
			'--deprecated-option-with-value-and-default-and-default-and-default-and-default': '--deprecated-option-with-value-and-default-and-default-and-default-and-default',
			'--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default': '--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default',
			'--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default-and-default': '--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default-and-default',
			'--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default-and-default-and-default': '--deprecated-option-with-value-and-default-and-default-and-default-and-default-and-default-and-default-and-default',
			'--deprecated-option-with-value-