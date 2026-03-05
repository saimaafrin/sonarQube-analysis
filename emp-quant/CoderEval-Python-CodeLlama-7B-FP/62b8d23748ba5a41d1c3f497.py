def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self.curr_size == 0:
		raise KeyError("popitem(): lru_cache is empty")
	# find the least frequently used item
	min_freq = sys.maxsize
	min_key = None
	for key, freq in self.freq_dict.items():
		if freq < min_freq:
			min_freq = freq
			min_key = key
	# remove the least frequently used item
	self.freq_dict.pop(min_key)
	self.cache_dict.pop(min_key)
	self.curr_size -= 1
	return min_key, self.cache_dict[min_key]