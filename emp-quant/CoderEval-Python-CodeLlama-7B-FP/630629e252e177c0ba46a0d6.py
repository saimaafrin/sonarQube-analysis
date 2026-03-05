def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	url = "https://{0}/.well-known/host-meta".format(host)
	response = requests.get(url)
	if response.status_code != 200:
		raise DiasporaError("Could not retrieve host-meta document from {0}".format(host))
	return xrd.parse(response.text)