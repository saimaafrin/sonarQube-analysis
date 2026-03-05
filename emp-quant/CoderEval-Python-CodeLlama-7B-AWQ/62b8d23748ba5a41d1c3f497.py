def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self.total == 0:
		raise KeyError('LFUCache is empty')
	min_key = min(self.counts, key=self.counts.get)
	del self.counts[min_key]
	del self.cache[min_key]
	self.total -= 1
	return min_key, self.cache[min_key]