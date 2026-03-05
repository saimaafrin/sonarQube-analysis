def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self.is_empty():
		raise KeyError("The dictionary is empty")
	else:
		key = self.keys[0]
		value = self.values[0]
		del self.keys[0]
		del self.values[0]
		return (key, value)