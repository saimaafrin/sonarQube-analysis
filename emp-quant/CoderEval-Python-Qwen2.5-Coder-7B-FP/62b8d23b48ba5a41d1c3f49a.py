def mru_cache(maxsize=128, typed=False):
# Import the required modules
	from functools import wraps, lru_cache

	# Define the wrapper function
	def wrapper(func):
		# Apply the lru_cache decorator from functools
		cached_func = lru_cache(maxsize=maxsize, typed=typed)(func)

		# Return the cached function
		return cached_func

	# Return the wrapper function
	return wrapper