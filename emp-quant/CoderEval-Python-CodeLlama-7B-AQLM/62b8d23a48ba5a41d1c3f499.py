def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.root is None:
		raise KeyError('LRU cache is empty')
	if self.root.prev is None:
		return self.root.key, self.root.value
	p = self.root.prev
	self.root.prev = p.prev
	if p.prev is not None:
		p.prev.next = self.root
	p.prev = None
	self.root = p
	self.root.next = None
	return p.key, p.value