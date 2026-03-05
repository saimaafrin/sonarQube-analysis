def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	if maxsize == 0:
		return lambda f: f

	def wrapper(*args, **kwds):
		if not hasattr(wrapper, 'cache'):
			wrapper.cache = {}
			wrapper.hits = 0
			wrapper.misses = 0
			wrapper.maxsize = maxsize
			wrapper.typed = typed
			wrapper.lock = threading.Lock()
		if typed:
			key = args + tuple(p for p in kwds.items())
		else:
			key = hash(frozenset(args))
			if kwds:
				key += frozenset(kwds.items())
		with wrapper.lock:
			if key in wrapper.cache:
				wrapper.hits += 1
				return wrapper.cache[key]
			wrapper.misses += 1
			result = f(*args, **kwds)
			if wrapper.maxsize == 1:
				wrapper.cache.clear()
			elif len(wrapper.cache) >= wrapper.maxsize:
				wrapper.cache.popitem()
			wrapper.cache[key] = result
			return result

	def cache_info():
		"""
		:return: a named tuple with the number of cache hits and misses
		"""
		with wrapper.lock:
			return wrapper.hits, wrapper.misses

	def cache_clear():
		"""
		Clear the cache and cache statistics
		"""
		with wrapper.lock:
			wrapper.cache.clear()
			wrapper.hits = 0
			wrapper.misses = 0

	wrapper.cache_info = cache_info
	wrapper.cache_clear = cache_clear
	return wrapper