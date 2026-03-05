def _replace_url_args(url, url_args):
# Split the URL into the base URL and the query string
	base_url, _, query_string = url.partition('?')

	# Parse the query string into a dictionary
	query_dict = dict(item.split('=') for item in query_string.split('&'))

	# Replace the values in the query dictionary with the values from url_args
	for key, value in url_args.items():
		if key in query_dict:
			query_dict[key] = value

	# Reconstruct the query string from the updated dictionary
	new_query_string = '&'.join(f'{key}={value}' for key, value in query_dict.items())

	# Return the modified URL
	return f'{base_url}?{new_query_string}'