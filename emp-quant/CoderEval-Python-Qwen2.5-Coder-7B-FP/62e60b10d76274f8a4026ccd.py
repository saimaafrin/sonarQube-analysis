def data(self, *keys):
# Check if any keys are provided
	if not keys:
		return self._data.keys()
	
	# Filter and return the specified keys
	return {key: self._data[key] for key in keys if key in self._data}