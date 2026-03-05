def popitem(self):
# Check if the dictionary is empty
	if not self:
		return None

	# Get the first key inserted (using next(iter(self)))
	first_key = next(iter(self))

	# Retrieve the value associated with the first key
	value = self[first_key]

	# Remove the key-value pair from the dictionary
	del self[first_key]

	# Return the key-value pair as a tuple
	return first_key, value