def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorate(func):
		def wrapper(*args, **kwargs):
			if lock is None:
				lock = threading.Lock()
			key = key(*args, **kwargs)
			with lock:
				if key in cache:
					return cache[key]
				else:
					result = func(*args, **kwargs)
					cache[key] = result
					return result
		return wrapper
	return decorate