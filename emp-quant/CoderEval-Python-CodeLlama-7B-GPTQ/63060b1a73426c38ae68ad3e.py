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
	plugin_spec_dict['config']['type'] = 'file'
	plugin_spec_dict['config']['path'] = ''
	plugin_spec_dict['config']['default'] = ''
	plugin_spec_dict['config']['description'] = ''
	plugin_spec_dict['config']['required'] = False
	plugin_spec_dict['config']['example'] = ''
	plugin_spec_dict['config']['options'] = []
	plugin_spec_dict['config']['options'][0]['name'] = ''
	plugin_spec_dict['config']['options'][0]['value'] = ''
	plugin_spec_dict['config']['options'][0]['description'] = ''
	plugin_spec_dict['config']['options'][0]['required'] = False
	plugin_spec_dict['config']['options'][0]['example'] = ''
	plugin_spec_dict['config']['options'][0]['options'] = []
	plugin_spec_dict['config']['options'][0]['options'][0]['name'] = ''
	plugin_spec_dict['config']['options'][0]['options'][0]['value'] = ''
	plugin_spec_dict['config']['options'][0]['options'][0]['description'] = ''
	plugin_spec_dict['config']['options'][0]['options'][0]['required'] = False
	plugin_spec_dict['config']['options'][0]['options'][0]['example'] = ''
	plugin_spec_