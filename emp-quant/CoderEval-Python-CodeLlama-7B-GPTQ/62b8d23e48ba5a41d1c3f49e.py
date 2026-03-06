def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.is_empty():
		raise KeyError("The dictionary is empty")
	else:
		key = self.__choice()
		value = self[key]
		del self[key]
		return (key, value)