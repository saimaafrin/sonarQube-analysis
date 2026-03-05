def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	children = node.children
	if children is None:
		return {}
	else:
		return dict([(child.tag, child) for child in children])