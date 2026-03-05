def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for key in nodes:
		if key in result:
			if isinstance(result[key], MappingNode):
				result[key] = deep_merge_nodes({key: result[key], key: nodes[key]})
			else:
				result[key] = nodes[key]
		else:
			result[key] = nodes[key]
	return result