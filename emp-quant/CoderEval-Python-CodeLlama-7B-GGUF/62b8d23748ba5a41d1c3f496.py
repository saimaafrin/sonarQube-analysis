def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	if maxsize <= 0:
		raise ValueError("maxsize must be positive")

	class _LFUCache(dict):
		def __init__(self, maxsize, typed):
			self.maxsize = maxsize
			self.typed = typed
			self.hits = self.misses = 0
			self.queue = []
			self.mapping = {}
			self.size = 0

		def __contains__(self, key):
			return key in self.mapping

		def __getitem__(self, key):
			self.hits += 1
			return dict.__getitem__(self, key)

		def __setitem__(self, key, value):
			if key in self.mapping:
				self.queue.remove(self.mapping[key])
			self.queue.append(key)
			self.mapping[key] = len(self.queue) - 1
			while len(self.queue) > self.maxsize:
				key = self.queue.pop(0)
				del self.mapping[key]
				dict.__delitem__(self, key)
			dict.__setitem__(self, key, value)
			self.size = len(self)

		def __delitem__(self, key):
			dict.__delitem__(self, key)
			del self.mapping[key]
			self.size = len(self)

		def __repr__(self):
			return "<%s %r>" % (self.__class__.__name__, self.mapping)

		def __len__(self):
			return self.size

		def get(self, key, default=None):
			"""
			Return the value for `key` if `key` is in the cache, else
			return `default`. If `default` is not given, return
			`None` if `key` is not in the cache.