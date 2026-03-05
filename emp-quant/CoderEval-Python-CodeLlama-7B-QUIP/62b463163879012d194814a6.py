def files_list_from_zipfile(zip_path):
	"""
	Return the files in the given zip path.
	"""
	zip_file = zipfile.ZipFile(zip_path)
	return zip_file.namelist()