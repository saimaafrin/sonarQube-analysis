def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
			def wrapper(*args, **kwargs):
			key = key(*args, **kwargs)
			if key in cache:
				return cache[key]
			else:
				with lock:
					if key in cache:
						return cache[key]
					else:
						result = func(*args, **kwargs)
						cache[key] = result
						return result
		return wrapper
	return decorator