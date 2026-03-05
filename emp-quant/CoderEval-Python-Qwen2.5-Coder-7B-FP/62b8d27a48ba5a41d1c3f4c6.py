def cached(cache, key=hashkey, lock=None):
# Create a new decorator function
	def decorator(func):
		# Define the wrapper function that will be called instead of func
		def wrapper(*args, **kwargs):
			# Generate a unique key for this call based on args and kwargs
			k = key(args, kwargs)
			# Check if the result is already in the cache
			if k not in cache:
				# If not, call the original function and store the result in the cache
				result = func(*args, **kwargs)
				cache[k] = result
			else:
				# If it is, just return the cached result
				result = cache[k]
			return result
		# Return the wrapper function
		return wrapper
	# Return the decorator function
	return decorator