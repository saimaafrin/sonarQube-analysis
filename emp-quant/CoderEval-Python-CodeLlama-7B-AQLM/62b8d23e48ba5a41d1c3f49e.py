def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.size == 0:
		raise KeyError("The dictionary is empty")
	else:
		return self.__choice()