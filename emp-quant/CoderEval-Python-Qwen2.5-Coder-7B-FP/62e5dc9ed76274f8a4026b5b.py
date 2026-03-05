def deprecated(message):
# Define the decorator function
	def decorator(func):
		# Add a docstring to the decorated function
		func.__doc__ = f"{func.__doc__}\n\n**Deprecated:** {message}"
		# Return the decorated function
		return func
	# Return the decorator function
	return decorator