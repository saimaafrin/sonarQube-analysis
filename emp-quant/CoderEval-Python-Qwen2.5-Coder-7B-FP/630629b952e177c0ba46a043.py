def get_nodeinfo_well_known_document(url, document_path=None):
# Check if the document path is provided
	if document_path:
		# If it is, return a dictionary with both URL and document path
		return {
			"url": url,
			"document_path": document_path
		}
	else:
		# If not, return only the URL in the dictionary
		return {
			"url": url
		}