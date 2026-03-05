def xml_children_as_dict(node):
# Create an empty dictionary to store the child nodes
	children = {}
	
	# Iterate over each child node in the XML element
	for child in node:
		# Check if the child node's tag is already in the dictionary
		if child.tag not in children:
			# If not, add it with its text content as the value
			children[child.tag] = child.text.strip()
		else:
			# If the tag is already present, append the text content to the existing value
			children[child.tag] += " " + child.text.strip()
	
	return children