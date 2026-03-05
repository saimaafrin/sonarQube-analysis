def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
			def wrapper(*args, **kwargs):
			if lock is not None:
				lock.acquire()
			try:
				result = cache.get(key(*args, **kwargs))
				if result is None:
					result = func(*args, **kwargs)
					cache.set(key(*args, **kwargs), result)
				return result
			finally:
				if lock is not None:
					lock.release()
		return wrapper
	return decorate