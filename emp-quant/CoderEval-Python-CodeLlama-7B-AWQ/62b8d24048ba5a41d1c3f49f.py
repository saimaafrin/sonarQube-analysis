def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	cache = TTLCache(maxsize, ttl, timer, typed)
	def decorator(func):
		"""
		Decorator function.
		"""
		def wrapper(*args, **kwargs):
			"""
			Wrapper function.
			"""
			key = (args, tuple(kwargs.items()))
			try:
				result, expire = cache[key]
				if timer() < expire:
					return result
			except KeyError:
				result = func(*args, **kwargs)
				cache[key] = (result, timer() + ttl)
				return result
			except TypeError:
				# unhashable key
				pass
			result = func(*args, **kwargs)
			cache[key] = (result, timer() + ttl)
			return result
		wrapper.__wrapped__ = func
		wrapper.__name__ = func.__name__
		wrapper.__doc__ = func.__doc__
		wrapper.__dict__.update(func.__dict__)
		return wrapper
	return decorator