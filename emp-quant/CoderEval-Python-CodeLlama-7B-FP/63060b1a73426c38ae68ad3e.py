def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec_dict = {}
	plugin_spec_dict['name'] = plugin_dir.split('/')[-1]
	plugin_spec_dict['version'] = '0.0.0'
	plugin_spec_dict['description'] = ''
	plugin_spec_dict['author'] = ''
	plugin_spec_dict['license'] = ''
	plugin_spec_dict['url'] = ''
	plugin_spec_dict['tags'] = []
	plugin_spec_dict['requires'] = []
	plugin_spec_dict['provides'] = []
	plugin_spec_dict['conflicts'] = []
	plugin_spec_dict['dependencies'] = []
	plugin_spec_dict['config'] = {}
	plugin_spec_dict['config_schema'] = {}
	plugin_spec_dict['config_defaults'] = {}
	plugin_spec_dict['config_help'] = {}
	plugin_spec_dict['config_types'] = {}
	plugin_spec_dict['config_options'] = {}
	plugin_spec_dict['config_required'] = {}
	plugin_spec_dict['config_hidden'] = {}
	plugin_spec_dict['config_advanced'] = {}
	plugin_spec_dict['config_order'] = {}
	plugin_spec_dict['config_group'] = {}
	plugin_spec_dict['config_group_order'] = {}
	plugin_spec_dict['config_group_description'] = {}
	plugin_spec_dict['config_group_hidden'] = {}
	plugin_spec_dict['config_group_advanced'] = {}
	plugin_spec_dict['config_group_required'] = {}
	plugin_spec_dict['config_group_default'] = {}
	plugin_spec_dict['config_group_options'] = {}
	plugin_spec_dict['config_group_order'] = {}
	plugin_spec_dict['config_group_description'] = {}
	plugin_spec_dict['config_group_hidden'] = {}
	plugin_spec_dict['config_group_advanced'] = {}
	plugin_spec_dict['config_group_required'] = {}
	plugin_