def unit_of_work(metadata=None, timeout=None):
# Decorator function
	def decorator(func):
		# Set the metadata attribute of the decorated function
		func.metadata = metadata
		# Set the timeout attribute of the decorated function
		func.timeout = timeout
		# Return the decorated function
		return func

	# Return the decorator function
	return decorator