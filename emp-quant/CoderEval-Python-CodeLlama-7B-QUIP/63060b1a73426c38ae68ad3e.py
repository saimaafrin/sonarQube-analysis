def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec = {}
	plugin_spec['name'] = plugin_dir.name
	plugin_spec['version'] = plugin_dir.version
	plugin_spec['description'] = plugin_dir.description
	plugin_spec['author'] = plugin_dir.author
	plugin_spec['license'] = plugin_dir.license
	plugin_spec['url'] = plugin_dir.url
	plugin_spec['tags'] = plugin_dir.tags
	plugin_spec['requires'] = plugin_dir.requires
	plugin_spec['requires_python'] = plugin_dir.requires_python
	plugin_spec['classifiers'] = plugin_dir.classifiers
	plugin_spec['platforms'] = plugin_dir.platforms
	plugin_spec['provides'] = plugin_dir.provides
	plugin_spec['obsoletes'] = plugin_dir.obsoletes
	plugin_spec['provides_extra'] = plugin_dir.provides_extra
	plugin_spec['requires_dist'] = plugin_dir.requires_dist
	plugin_spec['requires_dist_extras'] = plugin_dir.requires_dist_extras
	plugin_spec['requires_dist_extras_spec'] = plugin_dir.requires_dist_extras_spec
	plugin_spec['requires_dist_extras_version'] = plugin_dir.requires_dist_extras_version
	plugin_spec['requires_dist_extras_version_spec'] = plugin_dir.requires_dist_extras_version_spec
	plugin_spec['requires_dist_extras_version_spec_spec'] = plugin_dir.requires_dist_extras_version_spec_spec
	plugin_spec['requires_dist_extras_version_spec_spec_spec'] = plugin_dir.requires_dist_extras_version_spec_spec_spec
	plugin_spec['requires_dist_extras_version_spec_spec_spec_spec'] = plugin_dir.requires_dist_extras_version_spec_spec_