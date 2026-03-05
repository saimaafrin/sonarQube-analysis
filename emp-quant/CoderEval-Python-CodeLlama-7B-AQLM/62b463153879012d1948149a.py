def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	result = {}
	for xml in xmls:
		result[xml] = []
	for file in files:
		if file.endswith(".xml"):
			result[file].append(file)
	return result