def validate_value(value):
# Define a dictionary of regular expressions for each data type
	regex_dict = {
		'int': r'^-?\d+$',
		'float': r'^-?\d+\.\d+$',
		'str': r'^[a-zA-Z0-9\s]+$',
		'date': r'^\d{4}-\d{2}-\d{2}$'
	}
	
	# Get the data type from the user input
	data_type = input("Enter the data type (int, float, str, date): ")
	
	# Check if the data type is valid
	if data_type not in regex_dict:
		print("Invalid data type")
		return False
	
	# Validate the value using the corresponding regular expression
	if re.match(regex_dict[data_type], value):
		return True
	else:
		return False