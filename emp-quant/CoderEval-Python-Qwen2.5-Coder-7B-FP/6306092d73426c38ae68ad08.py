def _get_conditionally_required_args(self, command_name, options_spec,
                                         args):
# Get all required arguments for this command
	required_args = self._get_required_args(command_name, options_spec)

	# Filter out those that are not required when a certain condition is met
	conditionally_required_args = []
	for arg in required_args:
		if 'required_when' in options_spec[arg]:
			condition = options_spec[arg]['required_when']
			if self._is_condition_met(condition, args):
				conditionally_required_args.append(arg)

	return conditionally_required_args