def _explore_folder(folder):
# Get all files in the folder
	files = os.listdir(folder)
	
	# Filter out directories and get only files
	files = [f for f in files if os.path.isfile(os.path.join(folder, f))]
	
	# Group files by XML filename
	grouped_files = {}
	for file in files:
		xml_filename = _get_xml_filename_from_file(file)
		if xml_filename not in grouped_files:
			grouped_files[xml_filename] = []
		grouped_files[xml_filename].append(file)
	
	return grouped_files