def get(self, key, default=None):
# Check if the key exists in the dictionary
	if key in self.data:
		return self.data[key]
	else:
		return default