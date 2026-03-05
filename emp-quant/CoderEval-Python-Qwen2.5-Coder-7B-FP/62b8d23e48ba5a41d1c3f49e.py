def popitem(self):
# Check if the dictionary is empty
	if not self:
		return None

	# Choose a random key from the dictionary
	random_key = self.__choice(list(self.keys()))

	# Get the corresponding value using the chosen key
	value = self[random_key]

	# Remove the (key, value) pair from the dictionary
	del self[random_key]

	# Return the removed (key, value) pair
	return random_key, value