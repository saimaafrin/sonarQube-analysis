def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("Expected a type, got %r" % (candidate,))
	if not issubclass(candidate, iface):
		raise TypeError("Expected a subclass of %r, got %r" % (iface, candidate))
	if not candidate.is_abstract:
		return True
	if tentative:
		return True
	raise TypeError("Expected a concrete type, got %r" % (candidate,))