def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def deprecated_decorator(func):
		"""
		Return a decorated function for deprecating functions and methods.
		"""
		def deprecated_func(*args, **kwargs):
			"""
			Return a decorated function for deprecating functions and methods.
			"""
			warnings.warn(message, DeprecationWarning)
			return func(*args, **kwargs)
		return deprecated_func
	return deprecated_decorator