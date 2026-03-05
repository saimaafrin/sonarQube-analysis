def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not fixity:
		return
	if not isinstance(fixity, dict):
		self.error("fixity block is not a dictionary")
	if not isinstance(fixity.get("fixity"), list):
		self.error("fixity block is not a list")
	for fixity_entry in fixity.get("fixity"):
		if not isinstance(fixity_entry, dict):
			self.error("fixity entry is not a dictionary")
		if not isinstance(fixity_entry.get("file"), str):
			self.error("fixity entry file is not a string")
		if not isinstance(fixity_entry.get("checksum"), str):
			self.error("fixity entry checksum is not a string")
		if not isinstance(fixity_entry.get("algorithm"), str):
			self.error("fixity entry algorithm is not a string")
		if not isinstance(fixity_entry.get("size"), int):
			self.error("fixity entry size is not an integer")
		if not isinstance(fixity_entry.get("mime"), str):
			self.error("fixity entry mime is not a string")
		if not isinstance(fixity_entry.get("sha256"), str):
			self.error("fixity entry sha256 is not a string")
		if not isinstance(fixity_entry.get("sha512"), str):
			self.error("fixity entry sha512 is not a string")
		if not isinstance(fixity_entry.get("sha1"), str):
			self.error("fixity entry sha1 is not a string")
		if not isinstance(fixity_entry.get("md5"), str):
			self.error("fixity entry md5 is not a string")
		if not isinstance(fixity_entry.get("sha256_base64"), str):
			self.error("fixity entry sha256_base64 is not a