def add_rendition(self, lang, file_path):
# Check if the language already exists in the renditions dictionary
	if lang not in self._renditions:
		self._renditions[lang] = []
	
	# Append the file path to the list of renditions for the given language
	self._renditions[lang].append(file_path)