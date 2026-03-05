def regex_dict(item):
regex_item = {}
	for key, value in item.items():
		# Convert wildcard to regex
		regex_key = key.replace('*', '.*')
		regex_item[regex_key] = value
	return regex_item