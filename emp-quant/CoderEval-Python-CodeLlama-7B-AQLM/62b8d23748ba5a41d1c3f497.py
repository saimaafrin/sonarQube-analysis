def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self:
		raise KeyError('LRU cache is empty')
	self._check_key(self.root.key)
	return self.root.key, self.root.value