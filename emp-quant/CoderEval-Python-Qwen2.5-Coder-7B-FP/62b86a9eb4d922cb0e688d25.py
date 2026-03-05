def _get_resource_name_regex():
# The resource names must be alphanumeric and can contain hyphens, underscores or dots.
	return r"^[a-zA-Z0-9][a-zA-Z0-9\-_\.]*$"