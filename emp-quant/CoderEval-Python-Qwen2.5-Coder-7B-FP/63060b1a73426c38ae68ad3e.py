def get_plugin_spec_flatten_dict(plugin_dir):
plugin_info = {}
	for root, dirs, files in os.walk(plugin_dir):
		for file in files:
			if file.endswith('.yaml'):
				file_path = os.path.join(root, file)
				with open(file_path, 'r') as f:
					data = yaml.safe_load(f)
					plugin_info.update(data)
	return plugin_info