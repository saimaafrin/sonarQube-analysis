def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	try:
		return xrd.retrieve(host)
	except xrd.XRDParseError:
		raise DiasporaError("Could not parse host-meta document")