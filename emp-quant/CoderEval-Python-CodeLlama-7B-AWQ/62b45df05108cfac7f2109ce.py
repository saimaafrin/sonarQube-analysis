def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if path == "/":
		return True
	else:
		return self.exists(path) and self.is_ocfl_object(path)

	def is_ocfl_object(self, path):
		"""
		Returns True if path is an OCFL object, False otherwise.
		"""
		return self.exists(path + "/" + OCFL_CONFIG_FILE)

	def is_ocfl_root(self, path):
		"""
		Returns True if path is the root of an OCFL repository, False otherwise.
		"""
		return self.exists(path + "/" + OCFL_ROOT_FILE)

	def is_ocfl_file(self, path):
		"""
		Returns True if path is an OCFL file, False otherwise.
		"""
		return self.exists(path) and not self.is_ocfl_object(path)

	def is_ocfl_directory(self, path):
		"""
		Returns True if path is an OCFL directory, False otherwise.
		"""
		return self.exists(path) and self.is_ocfl_object(path)

	def is_ocfl_file_or_directory(self, path):
		"""
		Returns True if path is an OCFL file or directory, False otherwise.
		"""
		return self.exists(path) and not self.is_ocfl_object(path)

	def is_ocfl_file_or_object(self, path):
		"""
		Returns True if path is an OCFL file or object, False otherwise.
		"""
		return self.exists(path) and not self.is_ocfl_root(path)

	def is_ocfl_object_or_root(self, path):
		"""
		Returns True if path is an OCFL object or root, False otherwise.
		"""
		return self.exists(path) and not self.is_ocfl_file(