def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec = {}
	plugin_spec['name'] = plugin_dir.split('/')[-1]
	plugin_spec['version'] = '0.0.0'
	plugin_spec['description'] = ''
	plugin_spec['author'] = ''
	plugin_spec['license'] = ''
	plugin_spec['url'] = ''
	plugin_spec['email'] = ''
	plugin_spec['keywords'] = []
	plugin_spec['dependencies'] = []
	plugin_spec['optional_dependencies'] = []
	plugin_spec['entry_points'] = {}
	plugin_spec['scripts'] = []
	plugin_spec['data_files'] = []
	plugin_spec['package_data'] = {}
	plugin_spec['packages'] = []
	plugin_spec['package_dir'] = {}
	plugin_spec['include_package_data'] = False
	plugin_spec['install_requires'] = []
	plugin_spec['extras_require'] = {}
	plugin_spec['python_requires'] = ''
	plugin_spec['classifiers'] = []
	plugin_spec['platforms'] = []
	plugin_spec['obsoletes'] = []
	plugin_spec['provides'] = []
	plugin_spec['requires'] = []
	plugin_spec['requires_dist'] = []
	plugin_spec['provides_dist'] = []
	plugin_spec['requires_python'] = ''
	plugin_spec['requires_external'] = []
	plugin_spec['project_urls'] = {}
	plugin_spec['download_url'] = ''
	plugin_spec['download_url_version'] = ''
	plugin_spec['download_url_md5'] = ''
	plugin_spec['download_url_sha256'] = ''
	plugin_spec['download_url_sha512'] = ''
	plugin_spec['download_url_size'] = ''
	plugin_spec['download_url_filename'] = ''
	plugin_spec['download_url_path'] = ''
	plugin_spec['download_url_platform'] = ''
	plugin_spec['download_url