def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("candidate must be a class")
	if not issubclass(candidate, iface):
		raise TypeError("candidate must be a subclass of %s" % iface)
	if not tentative:
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate, _Verified):
			raise TypeError("candidate must be a subclass of _Verified")
		if not issubclass(candidate