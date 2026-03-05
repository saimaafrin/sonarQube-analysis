def select_filenames_by_prefix(prefix, files):
# Initialize an empty list to store matching filenames
	matching_files = []

	# Iterate over each filename in the provided list of files
	for file in files:
		# Check if the current file starts with the specified prefix
		if file.startswith(prefix):
			# If it does, add the file to the list of matching files
			matching_files.append(file)

	# Return the list of matching files
	return matching_files