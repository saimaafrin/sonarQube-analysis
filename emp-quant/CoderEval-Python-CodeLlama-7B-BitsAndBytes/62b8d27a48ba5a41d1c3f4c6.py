def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
			def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			if lock:
				lock.acquire()
			try:
				if key in cache:
					return cache[key]
				else:
					result = func(*args, **kwargs)
					cache[key] = result
					return result
			finally:
				if lock:
					lock.release()
		return wrapper
	return decorator