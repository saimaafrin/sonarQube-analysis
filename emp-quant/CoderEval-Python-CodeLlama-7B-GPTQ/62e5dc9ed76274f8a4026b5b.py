def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def decorator(func):
		"""
		Decorator function for deprecating functions and methods.
		"""
		def wrapper(*args, **kwargs):
			"""
			Wrapper function for the deprecated function or method.
			"""
			print(message)
			return func(*args, **kwargs)
		return wrapper
	return decorator