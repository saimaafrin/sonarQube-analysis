def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
			"""
		Return a decorated function for deprecating functions and methods.
		"""
		def deprecated_func(*args, **kwargs):
			"""
			Return a decorated function for deprecating functions and methods.
			"""
			print(message)
			return func(*args, **kwargs)
		return deprecated_func
	return deprecated_decorator