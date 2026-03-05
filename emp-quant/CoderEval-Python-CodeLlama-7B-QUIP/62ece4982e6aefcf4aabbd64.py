def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if path.startswith(root):
		return path[len(root):]
	else:
		raise Exception("Path does not start with root")