def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.size() == 0:
		raise ValueError("popitem(): dictionary is empty")
	
	# Choose a random key
	key = self.__choice()
	
	# Remove the key from the dictionary
	self.remove(key)
	
	# Return the key and value
	return key, self[key]