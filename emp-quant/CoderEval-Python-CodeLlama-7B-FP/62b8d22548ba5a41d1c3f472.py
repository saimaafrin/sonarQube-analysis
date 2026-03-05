def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
			def wrapper(*args, **kwargs):
			if key is None:
				key = args
			if lock is None:
				lock = threading.Lock()
			with lock:
				if key not in cache:
					cache[key] = func(*args, **kwargs)
			return cache[key]
		return wrapper
	return decorator