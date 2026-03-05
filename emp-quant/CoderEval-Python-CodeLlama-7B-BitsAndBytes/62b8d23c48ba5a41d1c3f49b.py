def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self.curr is None:
		raise KeyError('popitem(): dictionary is empty')
	pair = self.curr
	self.curr = self.curr.prev
	if self.curr is not None:
		self.curr.next = None
	pair.prev = None
	return pair