def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			key = key(*args, **kwargs)
			if key in cache:
				return cache[key]
			else:
				if lock:
					lock.acquire()
				try:
					result = func(*args, **kwargs)
					cache[key] = result
					return result
				finally:
					if lock:
						lock.release()
					else:
						return result
		return wrapper
	return decorator