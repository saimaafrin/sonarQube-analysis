def _group_files_by_xml_filename(source, xmls, files):
# Create a dictionary to store the grouped files
	grouped_files = {}

	# Iterate over each XML file
	for xml_file in xmls:
		# Extract the base name of the XML file (without extension)
		xml_base_name = os.path.splitext(xml_file)[0]

		# Initialize an empty list for this XML file if it doesn't exist yet
		if xml_base_name not in grouped_files:
			grouped_files[xml_base_name] = []

		# Iterate over each file in the source directory
		for file in files:
			# Check if the file starts with the same base name as the XML file
			if file.startswith(xml_base_name):
				# Add the file to the corresponding list in the dictionary
				grouped_files[xml_base_name].append(file)

	return grouped_files