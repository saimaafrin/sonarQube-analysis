def files_list(path):
	"""
	Return the files in given path.
	"""
	files = []
	for file in os.listdir(path):
		if os.path.isfile(file):
			files.append(file)
	return files