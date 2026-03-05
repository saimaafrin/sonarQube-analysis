def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			if key(args, kwargs) in cache:
				return cache[key(args, kwargs)]
			else:
				with lock:
					if key(args, kwargs) in cache:
						return cache[key(args, kwargs)]
					else:
						result = func(*args, **kwargs)
						if key(args, kwargs) not in cache:
							cache[key(args, kwargs)] = result
						return result
		return wrapper
	return decorator