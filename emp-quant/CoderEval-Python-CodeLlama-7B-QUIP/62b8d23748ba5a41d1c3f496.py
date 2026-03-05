def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorator(obj):
		if typed:
			if isinstance(obj, (int, float, complex)):
				return obj
			raise TypeError("LFUCache can't cache '%s' object" % (type(obj),))
		if isinstance(obj, (int, float, complex)):
			return obj
		if not isinstance(obj, (int, float, complex)):
			raise TypeError("LFUCache can't cache '%s' object" % (type(obj),))
		if maxsize <= 0:
			raise ValueError("maxsize must be > 0")
		if maxsize > 128:
			raise ValueError("maxsize must be <= 128" % (maxsize,))
		if maxsize < 128:
			raise ValueError("maxsize must be >= 128" % (maxsize,))
		if maxsize > 128:
			raise ValueError("maxsize must be <= 128" % (maxsize,))
		if maxsize < 128:
			raise ValueError("maxsize must be >= 128" % (maxsize,))
		if maxsize > 128:
			raise ValueError("maxsize must be <= 128" % (maxsize,))
		if maxsize < 128:
			raise ValueError("maxsize must be >= 128" % (maxsize,))
		if maxsize > 128:
			raise ValueError("maxsize must be <= 128" % (maxsize,))
		if maxsize < 128:
			raise ValueError("maxsize must be >= 128" % (maxsize,))
		if maxsize > 128:
			raise ValueError("maxsize must be <= 128" % (maxsize,))
		if maxsize < 128:
			raise ValueError("maxsize must be >= 128" % (max