def check_digests_present_and_used(self, manifest_files, digests_used):
manifest_digests = self.get_manifest_digests(manifest_files)
	for digest in digests_used:
		if digest not in manifest_digests:
			self.error(f"Digest {digest} is used but not present in any manifest file.")
		else:
			# Check if the digest is actually used
			digest_used_in_file = False
			for file in manifest_files:
				if digest in self.get_file_content(file):
					digest_used_in_file = True
					break
			if not digest_used_in_file:
				self.error(f"Digest {digest} is present in a manifest file but not used in any file.")

	def get_manifest_digests(self, manifest_files):
		"""
		Get all unique digests from the manifest files.
		"""
		digests = set()
		for file in manifest_files:
			content = self.get_file_content(file)
			digests.update(content.split())
		return digests

	def get_file_content(self, file_path):
		"""
		Read the content of a file.
		"""
		with open(file_path, 'r') as file:
			return file.read()

	def error(self, message):
		"""
		Set an error message in the class.
		"""
		self.error_message = message
```

This code snippet defines a method `check_digests_present_and_used` that checks whether all digests required by the system are present in the manifest files and are used in at least one file. It uses helper methods to retrieve the digests from the manifest files and to read the content of the files. If a digest is found to be missing or unused, it sets an error message in the class. The `error` method is used to store the error message.