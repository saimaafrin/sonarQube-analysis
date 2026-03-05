def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
			def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			if lock:
				lock.acquire()
			try:
				result = cache[key]
			except KeyError:
				result = func(*args, **kwargs)
				cache[key] = result
			if lock:
				lock.release()
			return result
		return wrapper
	return decorator