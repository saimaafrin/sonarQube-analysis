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
	if frequency is None or frequency.lower() == "always":
		return None
	else:
		try:
			number = int(frequency.split()[0])
			unit = frequency.split()[1]
			return datetime.timedelta(**{unit: number})
		except:
			raise ValueError("Invalid frequency: %s" % frequency)