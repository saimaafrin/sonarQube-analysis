def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec_dict = {}
	plugin_spec_dict['name'] = plugin_dir.split('/')[-1]
	plugin_spec_dict['version'] = '0.0.1'
	plugin_spec_dict['description'] = 'No description'
	plugin_spec_dict['author'] = 'No author'
	plugin_spec_dict['license'] = 'No license'
	plugin_spec_dict['url'] = 'No url'
	plugin_spec_dict['keywords'] = []
	plugin_spec_dict['dependencies'] = []
	plugin_spec_dict['requires'] = []
	plugin_spec_dict['requires_python'] = '>=3.6'
	plugin_spec_dict['classifiers'] = []
	plugin_spec_dict['packages'] = []
	plugin_spec_dict['package_dir'] = {}
	plugin_spec_dict['package_data'] = {}
	plugin_spec_dict['data_files'] = []
	plugin_spec_dict['scripts'] = []
	plugin_spec_dict['entry_points'] = {}
	plugin_spec_dict['ext_modules'] = []
	plugin_spec_dict['cmdclass'] = {}
	plugin_spec_dict['options'] = {}
	plugin_spec_dict['zip_safe'] = False
	plugin_spec_dict['python_requires'] = '>=3.6'
	plugin_spec_dict['install_requires'] = []
	plugin_spec_dict['setup_requires'] = []
	plugin_spec_dict['tests_require'] = []
	plugin_spec_dict['test_suite'] = None
	plugin_spec_dict['use_scm_version'] = False
	plugin_spec_dict['setup_requires'] = []
	plugin_spec_dict['project_urls'] = {}
	plugin_spec_dict['python_requires'] = '>=3.6'
	plugin_spec_dict['use_scm_version'] = False
	plugin_spec_dict['use_scm_version'] = False
	plugin_spec_dict['use_scm_version'] =