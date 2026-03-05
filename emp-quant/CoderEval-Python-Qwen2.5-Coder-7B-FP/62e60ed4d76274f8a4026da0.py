def keys(self):
# Check if the __keys attribute exists in the class
	if hasattr(self, '__keys'):
		# Return the value of the __keys attribute as a list
		return self.__keys
	else:
		# If __keys does not exist, return an empty list
		return []