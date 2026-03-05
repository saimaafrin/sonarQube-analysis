def deep_merge_nodes(nodes):
merged = {}
	for node in nodes:
		if isinstance(node, MappingNode):
			for key, value in node.items():
				if key not in merged or not isinstance(merged[key], MappingNode) or not isinstance(value, MappingNode):
					merged[key] = value
				else:
					merged[key] = deep_merge_nodes([merged[key], value])
	return merged