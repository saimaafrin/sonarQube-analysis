def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "http://%s/.well-known/webfinger?resource=acct:%s" % (handle, handle)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data