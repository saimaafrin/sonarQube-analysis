def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.root is None:
		raise KeyError('LRU cache is empty')
	return self.remove_node(self.root)