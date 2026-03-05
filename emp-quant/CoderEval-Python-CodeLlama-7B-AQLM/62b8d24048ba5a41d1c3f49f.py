def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	if maxsize <= 0:
		raise ValueError("maxsize must be a positive integer")
	if ttl <= 0:
		raise ValueError("ttl must be a positive integer")

	cache = TTLCache(maxsize, ttl, timer, typed)

	def decorating_function(user_function):
		@wraps(user_function)
		def wrapper(*args, **kwargs):
			# cache_key = args + tuple(kwargs.items())
			cache_key = args + tuple(kwargs.items())
			try:
				result = cache[cache_key]
			except KeyError:
				result = user_function(*args, **kwargs)
				cache[cache_key] = result
			return result

		return wrapper

	return decorating_function