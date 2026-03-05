def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for node in nodes:
		for key, value in node.items():
			if key not in result:
				result[key] = value
			elif isinstance(value, MappingNode):
				result[key] = deep_merge_nodes([result[key], value])
			else:
				result[key] = value
	return result