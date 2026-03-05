def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block is not a dictionary")
		return
	if not all(isinstance(key, str) for key in fixity.keys()):
		self.error("Fixity block keys are not strings")
		return
	if not all(isinstance(value, str) for value in fixity.values()):
		self.error("Fixity block values are not strings")
		return
	if not all(value.startswith("sha256:") for value in fixity.values()):
		self.error("Fixity block values are not SHA-256 hashes")
		return
	if not all(value in manifest_files for value in fixity.values()):
		self.error("Fixity block references files not listed in the manifest")
		return