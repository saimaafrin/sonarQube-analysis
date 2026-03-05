def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	data = {}
	for xml in xmls:
		data[xml] = []
	for file in files:
		if file in xmls:
			data[file].append(source[file])
	return data