def _eval_file(prefix, file_path):
# Check if the file path starts with the given prefix
	if not file_path.startswith(prefix):
		return None

	# Get the file extension
	file_extension = os.path.splitext(file_path)[1]

	# Check if the file extension is xml
	if file_extension == ".xml":
		return None

	# Check if the file extension is pdf
	elif file_extension == ".pdf":
		component_id = os.path.basename(file_path).split(".")[0]
		return {"component_id": component_id, "file_path": file_path}

	else:
		component_id = os.path.basename(file_path).split(".")[0]
		ftype = file_extension[1:]
		return {"component_id": component_id, "file_path": file_path, "ftype": ftype}