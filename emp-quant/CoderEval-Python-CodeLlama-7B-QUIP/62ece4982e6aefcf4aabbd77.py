def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
     datetime.timedelta instance.
     If the frequency is None or "always", return None.
     Raise ValueError if the given frequency cannot be parsed.
     For instance, given "3 timeunit", return datetime.timedelta(timeunit=3)

     @param frequency :  A frequency string "number timeunit"

    @return str, the corresponding datetime
	"""
	if frequency is None or frequency == "always":
		return None
	if frequency == "never":
		return None
	if frequency == "always":
		return None
	if frequency == "once":
		return datetime.timedelta(seconds=1)
	if frequency == "hourly":
		return datetime.timedelta(hours=1)
	if frequency == "daily":
		return datetime.timedelta(days=1)
	if frequency == "weekly":
		return datetime.timedelta(weeks=1)
	if frequency == "monthly":
		return datetime.timedelta(days=30)
	if frequency == "yearly":
		return datetime.timedelta(days=365)
	if frequency == "custom":
		return datetime.timedelta(days=1)
	raise ValueError("Frequency %s cannot be parsed" % frequency)