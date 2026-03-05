def parse_frequency(frequency):
# Check for special cases where frequency is None or "always"
	if frequency is None or frequency.lower() == "always":
		return None

	# Split the frequency into number and timeunit parts
	parts = frequency.split()
	if len(parts) != 2:
		raise ValueError("Invalid frequency format")

	number_str, timeunit = parts
	try:
		number = int(number_str)
	except ValueError:
		raise ValueError("Number part must be an integer")

	# Create a timedelta object based on the timeunit
	if timeunit == "seconds":
		return timedelta(seconds=number)
	elif timeunit == "minutes":
		return timedelta(minutes=number)
	elif timeunit == "hours":
		return timedelta(hours=number)
	elif timeunit == "days":
		return timedelta(days=number)
	else:
		raise ValueError("Unsupported timeunit: {}".format(timeunit))