def match_pubdate(node, pubdate_xpaths):
# Iterate over each xpath in the provided list
	for xpath in pubdate_xpaths:
		# Use the find method to search for elements matching the current xpath
		pubdates = node.find(xpath)
		# If any matches are found, return the first one
		if pubdates is not None:
			return pubdates
	# If no matches are found after checking all xpaths, return None
	return None