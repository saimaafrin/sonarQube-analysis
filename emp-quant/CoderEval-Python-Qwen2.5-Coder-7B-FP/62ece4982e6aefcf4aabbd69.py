def _replace_register(flow_params, register_number, register_value):
# Replace the value of the register
	flow_params[register_number] = flow_params[register_value]

	# Delete the old register value
	del flow_params[register_value]