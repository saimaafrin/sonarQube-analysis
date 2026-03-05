def register_vcs_handler(vcs, method):
# Decorator function
	def decorator(func):
		# Set the attribute on the function
		func.vcs = vcs
		func.method = method
		return func
	return decorator