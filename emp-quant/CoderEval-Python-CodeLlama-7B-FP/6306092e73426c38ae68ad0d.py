def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	                                    spec_option):
if type_name == "list":
		return self.create_list_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "dict":
		return self.create_dict_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "tuple":
		return self.create_tuple_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "set":
		return self.create_set_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "range":
		return self.create_range_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "choice":
		return self.create_choice_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "file":
		return self.create_file_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "directory":
		return self.create_directory_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "path":
		return self.create_path_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "url":
		return self.create_url_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "email":
		return self.create_email_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "ipv4":
		return self.create_ipv4_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "ipv6":
		return self.create_ipv6_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "ip":
		return self.create_ip_argumet_type