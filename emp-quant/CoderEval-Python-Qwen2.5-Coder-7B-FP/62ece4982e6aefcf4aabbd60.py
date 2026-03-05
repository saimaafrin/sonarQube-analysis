def size_to_bytes(size: str) -> int:
# Define the units and their corresponding byte values
	units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}

	# Split the input string into the numeric part and the unit part
	num_str, unit_str = size[:-2], size[-2:]

	# Convert the numeric part to an integer
	num = int(num_str)

	# Return the total number of bytes by multiplying the numeric part with the corresponding byte value
	return num * units[unit_str] if unit_str in units else None