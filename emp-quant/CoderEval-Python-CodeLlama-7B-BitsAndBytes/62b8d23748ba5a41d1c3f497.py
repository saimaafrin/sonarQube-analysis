def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if len(self.queue) == 0:
		raise KeyError("LRU cache is empty")
	key, value = self.queue.popleft()
	del self.cache[key]
	return key, value