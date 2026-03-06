def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(iface, type):
		raise TypeError("iface must be a class")
	if not isinstance(candidate, type):
		raise TypeError("candidate must be a class")
	if iface is candidate:
		return True
	if tentative:
		return False
	if not issubclass(candidate, iface):
		raise TypeError("candidate does not implement iface")
	return True