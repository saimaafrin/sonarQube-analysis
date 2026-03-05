def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
			cache = TTLCache(maxsize, ttl, timer, typed)
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs, typed)
			ret = cache.get(key)
			if ret is None:
				ret = user_function(*args, **kwargs)
				cache[key] = ret
			return ret
		return wrapper
	return decorating_function