def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		def wrapper(*args, **kw):
			# Get the key
			key = key(*args, **kw)
			# Get the cache
			cache = cache
			# Check if the key is in the cache
			if key in cache:
				# If it is, return the cached value
				return cache[key]
			# Otherwise, call the function and cache the result
			else:
				# Call the function
				result = func(*args, **kw)
				# Cache the result
				cache[key] = result
				# Return the result
				return result
		# Return the wrapper
		return wrapper
	# Return the decorator
	return decorator