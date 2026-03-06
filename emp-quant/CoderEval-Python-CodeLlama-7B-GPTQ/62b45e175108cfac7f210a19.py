def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block must be a dictionary")
		return
	if not "files" in fixity:
		self.error("Fixity block must have a 'files' key")
		return
	if not isinstance(fixity["files"], list):
		self.error("Fixity block 'files' key must be a list")
		return
	for file in fixity["files"]:
		if not isinstance(file, dict):
			self.error("Fixity block 'files' key must be a list of dictionaries")
			return
		if not "path" in file:
			self.error("Fixity block file must have a 'path' key")
			return
		if not isinstance(file["path"], str):
			self.error("Fixity block file 'path' key must be a string")
			return
		if not "checksum" in file:
			self.error("Fixity block file must have a 'checksum' key")
			return
		if not isinstance(file["checksum"], str):
			self.error("Fixity block file 'checksum' key must be a string")
			return
		if not "algorithm" in file:
			self.error("Fixity block file must have an 'algorithm' key")
			return
		if not isinstance(file["algorithm"], str):
			self.error("Fixity block file 'algorithm' key must be a string")
			return
		if not file["path"] in manifest_files:
			self.error("Fixity block file 'path' key must be a file listed in the manifest")
			return