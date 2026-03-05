def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.root is None:
		raise KeyError('LRU cache is empty')
	else:
		return self.remove(self.root.key)