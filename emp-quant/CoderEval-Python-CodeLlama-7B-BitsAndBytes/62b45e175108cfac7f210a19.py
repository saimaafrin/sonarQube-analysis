def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block is not a dictionary")
		return
	if not "files" in fixity:
		self.error("Fixity block does not contain a 'files' key")
		return
	if not isinstance(fixity["files"], list):
		self.error("Fixity block 'files' key is not a list")
		return
	for file in fixity["files"]:
		if not isinstance(file, dict):
			self.error("Fixity block 'files' key contains a non-dictionary value")
			return
		if not "path" in file:
			self.error("Fixity block 'files' key contains a dictionary without a 'path' key")
			return
		if not isinstance(file["path"], str):
			self.error("Fixity block 'files' key contains a dictionary with a non-string 'path' key")
			return
		if not "checksum" in file:
			self.error("Fixity block 'files' key contains a dictionary without a 'checksum' key")
			return
		if not isinstance(file["checksum"], str):
			self.error("Fixity block 'files' key contains a dictionary with a non-string 'checksum' key")
			return
		if not file["path"] in manifest_files:
			self.error("Fixity block references a file not listed in the manifest")
			return
		if not file["checksum"] in manifest_files[file["path"]]:
			self.error("Fixity block references a checksum not listed in the manifest")
			return
		if not "algorithm" in file:
			self.error("Fixity block 'files' key contains a dictionary without an 'algorithm' key")
			return
		if not isinstance(file["algorithm"], str):
			self.error("Fixity block 'files' key contains a dictionary with a non-string 'algorithm' key")