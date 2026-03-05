def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	try:
		return xrd.parse(urllib2.urlopen(host + "/.well-known/host-meta.json"))
	except urllib2.HTTPError, e:
		if e.code == 404:
			raise DiasporaError("Host %s does not support Diaspora" % host)
		else:
			raise