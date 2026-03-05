def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
			def wrapper(*args, **kwargs):
			print(message)
			return func(*args, **kwargs)
		return wrapper
	return decorator