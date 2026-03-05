def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if len(self.queue) == 0:
		return None
	else:
		item = self.queue.pop(0)
		del self.cache[item[0]]
		return item