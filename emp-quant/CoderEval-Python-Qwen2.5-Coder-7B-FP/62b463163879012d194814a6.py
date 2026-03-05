def files_list_from_zipfile(zip_path):
# Importing zipfile module
	import zipfile

	# Open the zip file
	with zipfile.ZipFile(zip_path, 'r') as zip_ref:
		# Extract all the contents into the directory
		return zip_ref.namelist() # Returns a list of all files and directories in the zip file.