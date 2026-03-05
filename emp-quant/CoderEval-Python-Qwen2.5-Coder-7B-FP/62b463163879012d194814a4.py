def _explore_zipfile(zip_path):
# Get a list of all files in the zipfile
	file_list = zipfile.ZipFile(zip_path).namelist()

	# Group the files by their XML filename
	grouped_files = _group_files_by_xml_filename(file_list)

	return grouped_files