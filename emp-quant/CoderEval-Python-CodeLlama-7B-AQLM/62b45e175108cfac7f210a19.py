def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("fixity block is not a dictionary")
		return
	if not isinstance(fixity["files"], list):
		self.error("fixity block does not contain a list of files")
		return
	for file in fixity["files"]:
		if not isinstance(file, dict):
			self.error("fixity block contains a file that is not a dictionary")
			return
		if not isinstance(file["path"], str):
			self.error("fixity block contains a file that does not contain a path")
			return
		if not isinstance(file["checksum"], str):
			self.error("fixity block contains a file that does not contain a checksum")
			return
		if not isinstance(file["size"], int):
			self.error("fixity block contains a file that does not contain a size")
			return
		if not isinstance(file["algorithm"], str):
			self.error("fixity block contains a file that does not contain an algorithm")
			return
		if not file["path"] in manifest_files:
			self.error("fixity block contains a file that is not listed in the manifest")
			return