def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = []
	for file in os.listdir(folder):
		if file.endswith('.xml'):
			files.append(os.path.join(folder, file))
	return _group_files_by_xml_filename(files)