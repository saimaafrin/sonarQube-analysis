def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "http://{0}/diaspora/webfinger?resource={1}".format(handle, handle)
	response = requests.get(url)
	if response.status_code == 200:
		return parse_diaspora_webfinger(response.text)
	else:
		return None