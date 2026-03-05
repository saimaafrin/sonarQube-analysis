def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	# Remove the `(key, value)` pair least frequently used.
	self.remove(self.queue.pop(0))
	return self.queue.pop(0)