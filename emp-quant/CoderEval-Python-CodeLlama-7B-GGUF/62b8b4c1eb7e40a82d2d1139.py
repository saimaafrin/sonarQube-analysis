def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("Expected a class, got %r" % (candidate,))
	if not issubclass(candidate, iface):
		raise TypeError("Expected a subclass of %r, got %r" % (iface, candidate))
	if not hasattr(candidate, "__implements__"):
		raise TypeError("Expected a class with a __implements__ attribute, got %r" % (candidate,))
	if not isinstance(candidate.__implements__, tuple):
		raise TypeError("Expected a class with a __implements__ attribute that is a tuple, got %r" % (candidate.__implements__,))
	if not all(isinstance(i, type) for i in candidate.__implements__):
		raise TypeError("Expected a class with a __implements__ attribute that is a tuple of types, got %r" % (candidate.__implements__,))
	if not all(issubclass(i, iface) for i in candidate.__implements__):
		raise TypeError("Expected a class with a __implements__ attribute that is a tuple of subclasses of %r, got %r" % (iface, candidate.__implements__))
	if not all(hasattr(candidate, i.__name__) for i in candidate.__implements__):
		raise TypeError("Expected a class with a __implements__ attribute that is a tuple of attributes, got %r" % (candidate.__implements__,))
	if not all(isinstance(getattr(candidate, i.__name__), i) for i in candidate.__implements__):
		raise TypeError("Expected a class with a __implements__ attribute that is a tuple of attributes that are instances of the corresponding types, got %r" % (candidate.__implements__,))
	if tentative:
		return True
	if not hasattr(candidate, "__verify__"):
		raise TypeError("Expected a class with a __verify__ attribute, got %r" % (candidate,))
	if not callable(candidate