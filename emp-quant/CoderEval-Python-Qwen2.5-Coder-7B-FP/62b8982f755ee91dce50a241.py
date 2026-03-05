def normalized(self):
# Convert all units of time to integers
	self.seconds = int(self.seconds)
	self.minutes = int(self.minutes)
	self.hours = int(self.hours)

	# Normalize the seconds, minutes, and hours
	if self.seconds >= 60:
		self.minutes += self.seconds // 60
		self.seconds %= 60

	if self.minutes >= 60:
		self.hours += self.minutes // 60
		self.minutes %= 60

	if self.hours >= 24:
		self.days += self.hours // 24
		self.hours %= 24

	return self