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
	elif type_name == "int":
		return self.create_int_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "float":
		return self.create_float_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "bool":
		return self.create_bool_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "str":
		return self.create_str_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "path":
		return self.create_path_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "file":
		return self.create_file_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "dir":
		return self.create_dir_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "json":
		return self.create_json_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "yaml":
		return self.create_yaml_argumet_type(subcommand, option_name, spec_option)
	elif type_name == "toml":
		return self.create_toml_argumet_type(subcommand, option_