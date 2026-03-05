def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self.check() == False:
		return None
	else:
		return self.pop()