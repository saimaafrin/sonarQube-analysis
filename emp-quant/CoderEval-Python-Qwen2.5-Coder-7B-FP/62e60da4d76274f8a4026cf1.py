def values(self, *keys):
# Check if keys are provided
	if not keys:
		return []

	# Filter and return the values based on the index
	return [self.data[self.index][key] for key in keys if key in self.data[self.index]]