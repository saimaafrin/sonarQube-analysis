def cachedmethod(cache, key=hashkey, lock=None):
# Decorator to wrap a method
	def decorator(method):
		# Define the wrapper function that will be called instead of the original method
		def wrapper(self, *args, **kwargs):
			# Generate a unique key for this method call based on its arguments and keyword arguments
			k = key(args, kwargs)
			# Check if the result is already in the cache
			if k not in cache:
				# If not, compute the result by calling the original method
				result = method(self, *args, **kwargs)
				# Store the result in the cache with the generated key
				cache[k] = result
			else:
				# If the result is already in the cache, retrieve it from there
				result = cache[k]
			# Return the result
			return result
		# Return the wrapper function
		return wrapper
	# Return the decorator function
	return decorator