def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def decorator(func):
		def deprecated_func(*args, **kwargs):
			print(func.__name__ + " is deprecated: " + message)
			return func(*args, **kwargs)
		return deprecated_func
	return decorator