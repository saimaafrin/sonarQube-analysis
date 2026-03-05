def files_list(path):
# Importing os module
	import os

	# List to store file names
	files = []

	# Loop through all files and directories in the given path
	for item in os.listdir(path):

		# Check if it is a file
		if os.path.isfile(os.path.join(path, item)):

			# Add file name to the list
			files.append(item)

	return files