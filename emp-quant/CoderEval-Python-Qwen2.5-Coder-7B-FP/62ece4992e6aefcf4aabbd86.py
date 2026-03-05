def _dump_string(obj, dumper=None):
# Importing yaml module here to avoid circular import
	import yaml
	return yaml.dump(obj, default_flow_style=False)