def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			if lock is not None:
				lock.acquire()
			try:
				keyval = key(args, kwargs)
				if keyval in cache:
					return cache[keyval]
				else:
					result = func(*args, **kwargs)
					cache[keyval] = result
					return result
			finally:
				if lock is not None:
					lock.release()
		return wrapper
	return decorator