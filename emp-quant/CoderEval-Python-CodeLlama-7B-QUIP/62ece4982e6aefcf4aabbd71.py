def regex_dict(item):
	"""
	Convert *.cpp keys to regex keys.
Given a dict where the keys are all filenames with wildcards,
convert only the keys into equivalent regexes and leave the values intact.

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes
	"""
	return {
		re.sub(r'^.*\.cpp$', r'^.*\.cpp$', k): v
		for k, v in item.items()
	}