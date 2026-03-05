def remove_ending_os_sep(input_list):
# Check if the input list is None and return an empty list if it is
	if input_list is None:
		return []

	# Initialize an empty list to store the modified strings
	result = []

	# Iterate over each string in the input list
	for item in input_list:
		# Check if the string's length is greater than 1 and if the last character is the pathname separator
		if len(item) > 1 and item[-1] == os.sep:
			# Remove the trailing pathname separator and append the modified string to the result list
			result.append(item[:-1])
		else:
			# Append the original string to the result list
			result.append(item)

	# Return the modified list
	return result