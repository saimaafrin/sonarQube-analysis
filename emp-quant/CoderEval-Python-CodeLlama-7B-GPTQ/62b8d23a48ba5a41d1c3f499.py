def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.curr is None:
		raise KeyError('LRU cache is empty')
	key = self.curr.key
	value = self.curr.value
	self.curr = self.curr.prev
	if self.curr is not None:
		self.curr.next = None
	self.remove(key)
	return key, value