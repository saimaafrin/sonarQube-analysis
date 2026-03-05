def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("candidate must be a type")
	if not isinstance(iface, type):
		raise TypeError("iface must be a type")
	if iface is candidate:
		return True
	if not issubclass(candidate, iface):
		return False
	if tentative:
		return True
	if not hasattr(candidate, "__bases__"):
		return False
	for base in candidate.__bases__:
		if verifyClass(iface, base):
			return True
	return False