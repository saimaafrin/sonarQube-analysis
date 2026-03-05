def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block is not a dictionary")
		return
	if not "fixity" in fixity:
		self.error("Fixity block does not contain 'fixity' key")
		return
	if not isinstance(fixity["fixity"], list):
		self.error("Fixity block does not contain a list of fixity values")
		return
	for fix in fixity["fixity"]:
		if not isinstance(fix, dict):
			self.error("Fixity block contains a non-dictionary value")
			return
		if not "file" in fix:
			self.error("Fixity block does not contain 'file' key")
			return
		if not isinstance(fix["file"], str):
			self.error("Fixity block does not contain a string value for 'file' key")
			return
		if not fix["file"] in manifest_files:
			self.error("Fixity block references a file that is not listed in the manifest")
			return
		if not "algorithm" in fix:
			self.error("Fixity block does not contain 'algorithm' key")
			return
		if not isinstance(fix["algorithm"], str):
			self.error("Fixity block does not contain a string value for 'algorithm' key")
			return
		if not "value" in fix:
			self.error("Fixity block does not contain 'value' key")
			return
		if not isinstance(fix["value"], str):
			self.error("Fixity block does not contain a string value for 'value' key")
			return
		if not "checksum" in fix:
			self.error("Fixity block does not contain 'checksum' key")
			return
		if not isinstance(fix["checksum"], str):
			self.error("Fixity block does not contain a string value for 'checksum' key")