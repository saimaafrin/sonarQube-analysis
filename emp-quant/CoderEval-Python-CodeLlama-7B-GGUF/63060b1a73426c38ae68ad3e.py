def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec_dict = {}
	plugin_spec_dict['name'] = plugin_dir.split('/')[-1]
	plugin_spec_dict['version'] = '0.0.0'
	plugin_spec_dict['description'] = ''
	plugin_spec_dict['author'] = ''
	plugin_spec_dict['email'] = ''
	plugin_spec_dict['url'] = ''
	plugin_spec_dict['license'] = ''
	plugin_spec_dict['keywords'] = []
	plugin_spec_dict['dependencies'] = []
	plugin_spec_dict['optional_dependencies'] = []
	plugin_spec_dict['entry_points'] = {}
	plugin_spec_dict['scripts'] = []
	plugin_spec_dict['gui_scripts'] = []
	plugin_spec_dict['gui_entry_points'] = {}
	plugin_spec_dict['data_files'] = []
	plugin_spec_dict['package_data'] = {}
	plugin_spec_dict['packages'] = []
	plugin_spec_dict['include_package_data'] = False
	plugin_spec_dict['package_dir'] = {}
	plugin_spec_dict['python_requires'] = ''
	plugin_spec_dict['classifiers'] = []
	plugin_spec_dict['platforms'] = []
	plugin_spec_dict['obsoletes'] = []
	plugin_spec_dict['provides'] = []
	plugin_spec_dict['requires'] = []
	plugin_spec_dict['project_urls'] = {}
	plugin_spec_dict['download_url'] = ''
	plugin_spec_dict['install_requires'] = []
	plugin_spec_dict['extras_require'] = {}
	plugin_spec_dict['setup_requires'] = []
	plugin_spec_dict['tests_require'] = []
	plugin_spec_dict['test_suite'] = ''
	plugin_spec_dict['zip_safe'] = False
	plugin_spec_dict['python_version'] = ''
	plugin_spec_dict['python_version_spec'] = ''
	plugin_spec_dict['python