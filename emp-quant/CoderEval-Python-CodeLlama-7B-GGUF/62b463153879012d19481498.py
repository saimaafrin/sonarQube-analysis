def files_list(path):
	"""
	Return the files in given path.
	"""
	return [f for f in listdir(path) if isfile(join(path, f))]