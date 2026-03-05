def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
			vcs.handlers[method] = func
		return func
	return decorator