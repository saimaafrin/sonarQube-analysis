def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = _group_files_by_xml_filename(folder)
	return files