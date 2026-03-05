def _fromutc(self, dt):
# Convert the naive datetime to an aware datetime in UTC
	utc_dt = dt.replace(tzinfo=timezone.utc)
	
	# Convert the UTC datetime to the desired timezone
	new_tz = timezone('America/New_York')  # Replace with your desired timezone
	local_dt = utc_dt.astimezone(new_tz)
	
	return local_dt