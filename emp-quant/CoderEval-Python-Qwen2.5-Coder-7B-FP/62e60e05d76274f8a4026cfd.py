def index(self, key):
# Check if the key is a string
	if isinstance(key, str):
		# Convert the string to an integer using its ASCII value
		return sum(ord(char) for char in key)
	else:
		# If the key is not a string, return it as is
		return key