def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			if lock is None:
				lock = threading.Lock()
			with lock:
				if key(*args, **kwargs) in cache:
					return cache[key(*args, **kwargs)]
				else:
					result = func(*args, **kwargs)
					cache[key(*args, **kwargs)] = result
					return result
		return wrapper
	return decorator