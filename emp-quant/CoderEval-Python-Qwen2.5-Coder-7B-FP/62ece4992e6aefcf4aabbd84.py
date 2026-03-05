def is_ipv4(target):
# Check if the target is a string
	if isinstance(target, str):
		# Split the target by '.'
		parts = target.split('.')
		# Check if there are exactly 4 parts
		if len(parts) == 4:
			# Check if all parts are digits and in the range of 0-255
			return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
	# Return False if the target is not a valid IPv4 address
	return False