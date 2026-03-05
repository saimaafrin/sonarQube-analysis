def dehydrate_timedelta(value):
# Check if the value is a timedelta object
	if isinstance(value, timedelta):
		# Extract days, seconds and microseconds from the timedelta object
		days = value.days
		seconds = value.seconds
		microseconds = value.microseconds

		# Calculate hours, minutes and remaining seconds from the total seconds
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		remaining_seconds = seconds % 60

		# Return a dictionary representing the timedelta structure
		return {
			'days': days,
			'hours': hours,
			'minutes': minutes,
			'seconds': remaining_seconds,
			'microseconds': microseconds
		}
	else:
		# Raise an error if the input is not a timedelta object
		raise ValueError("Input must be a timedelta object")