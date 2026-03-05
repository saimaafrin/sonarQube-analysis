def validate_key(key):
# Regular expressions for different types of keys
	key_regex = {
		"username": r'^[a-zA-Z0-9_]{3,20}$',
		"email": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
		"password": r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
	}

	# Check if the key is in the dictionary and if it matches the regex
	if key in key_regex:
		return re.match(key_regex[key], value) is not None
	else:
		return False