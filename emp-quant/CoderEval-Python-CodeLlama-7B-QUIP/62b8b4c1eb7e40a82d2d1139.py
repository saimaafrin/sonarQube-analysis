def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not candidate:
		return False
	if iface == candidate:
		return True
	if not hasattr(candidate, '__class__'):
		return False
	if tentative:
		return False
	if iface == candidate.__class__:
		return True
	if not hasattr(candidate, '__class__'):
		return False
	return verifyClass(iface, candidate.__class__, tentative=True)