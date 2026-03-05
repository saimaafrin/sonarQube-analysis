def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
			func.vcs = vcs
		func.method = method
		return func
	return decorator