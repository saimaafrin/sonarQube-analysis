def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self.curr is None:
		raise KeyError('dictionary is empty')
	key = self.curr.key
	value = self.curr.value
	self.curr = self.curr.prev
	self.curr.next = None
	self.size -= 1
	return (key, value)