def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	# The underlying data structure is a list, since we
	# want to keep insertion order.
	class LRUCache(list):
		def __init__(self, maxsize, typed):
			self.maxsize = maxsize
			self.typed = typed
			self.mapping = {}
		def __getitem__(self, key):
			# The ordering of the list is from least to most
			# recently used.
			if self.typed:
				value = list.__getitem__(self, self.mapping[key])
				return value
			else:
				for i in range(len(self)):
					if self.mapping[key] == i:
						value = list.__getitem__(self, i)
						return value
		def __setitem__(self, key, value):
			if self.typed:
				list.__setitem__(self, self.mapping[key], value)
			else:
				if key in self.mapping:
					del self.mapping[key]
					list.__setitem__(self, self.mapping[key], value)
				else:
					list.__setitem__(self, len(self), value)
					self.mapping[key] = len(self) - 1
			if len(self) > self.maxsize:
				# The list is full, we need to remove the
				# oldest item.
				del self.mapping[list.__getitem__(self, 0)]
				list.__delitem__(self, 0)
		def __contains__(self, key):
			return key in self.mapping
		def __len__(self):
			return len(self.mapping)
	def wrapper(func):
		wrapped = LRUCache(maxsize, typed)
		def wrapped_func(*args):
			key = args if typed else args[