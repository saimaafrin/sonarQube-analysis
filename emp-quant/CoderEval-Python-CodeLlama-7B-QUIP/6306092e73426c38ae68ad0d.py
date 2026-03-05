def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	if type_name == 'list':
		return self.create_list_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict':
		return self.create_dict_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'set':
		return self.create_set_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'tuple':
		return self.create_tuple_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_list':
		return self.create_dict_list_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_set':
		return self.create_dict_set_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_tuple':
		return self.create_dict_tuple_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_dict':
		return self.create_dict_dict_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_dict_list':
		return self.create_dict_dict_list_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_dict_set':
		return self.create_dict_dict_set_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_dict_tuple':
		return self.create_dict_dict_tuple_argumet_type(subcommand, type_name, option_name, spec_option)
	elif type_name == 'dict_dict_dict':
		return self.create_dict