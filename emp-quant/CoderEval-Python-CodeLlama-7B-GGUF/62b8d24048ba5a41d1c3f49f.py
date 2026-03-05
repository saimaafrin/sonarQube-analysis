def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	cache = TTLCache(maxsize, ttl, timer, typed)

	def decorating_function(*args, **kwargs):
		key = args if typed else (args, frozenset(kwargs.items()))
		return cache[key]

	return decorating_function