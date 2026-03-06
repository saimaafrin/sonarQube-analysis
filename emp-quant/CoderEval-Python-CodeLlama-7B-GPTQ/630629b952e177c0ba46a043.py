def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	nodeinfo = {
		"url": url,
		"document_path": document_path,
		"nodeinfo_document": None,
		"nodeinfo_document_json": None,
		"nodeinfo_document_json_pretty": None,
		"nodeinfo_document_json_pretty_sorted": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments_no_trailing_commas": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments_no_trailing_commas_no_leading_zeros": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments_no_trailing_commas_no_leading_zeros_no_trailing_whitespace": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments_no_trailing_commas_no_leading_zeros_no_trailing_whitespace_no_leading_whitespace": None,
		"nodeinfo_document_json_pretty_sorted_no_nulls_no_empty_strings_no_whitespace_no_comments_no_trailing_commas_no_leading_zeros_no_trailing_whitespace_no_leading_whitespace_