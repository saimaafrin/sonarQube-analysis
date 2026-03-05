def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	merged = {}
	for node in nodes:
		for key, value in node.items():
			if key not in merged:
				merged[key] = value
			elif isinstance(merged[key], MappingNode):
				merged[key] = deep_merge_nodes([merged[key], value])
			elif isinstance(value, MappingNode):
				merged[key] = deep_merge_nodes([merged[key], value])
			else:
				merged[key] = value
	return merged