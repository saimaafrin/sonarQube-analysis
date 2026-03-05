def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	# Get the files in the zip path.
	files = _get_files_in_zip_path(zip_path)
	
	# Group the files by their XML filename.
	groups = _group_files_by_xml_filename(files)
	
	# Return the groups.
	return groups