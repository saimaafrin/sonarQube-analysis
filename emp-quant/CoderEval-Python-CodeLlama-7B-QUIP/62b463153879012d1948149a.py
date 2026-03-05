def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	# Get the xmls
	xmls = xmls.split(',')
	
	# Group files by xmls
	groups = {}
	for xml in xmls:
		groups[xml] = []
	
	for file in files:
		if file.endswith('.xml'):
			for xml in xmls:
				if xml in file:
					groups[xml].append(file)
	
	return groups