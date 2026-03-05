def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	self.start = int(self.start)
	self.end = int(self.end)
	self.duration = int(self.duration)
	self.offset = int(self.offset)
	self.confidence = float(self.confidence)
	self.pause = int(self.pause)
	self.pause_duration = int(self.pause_duration)
	self.pause_offset = int(self.pause_offset)
	self.pause_confidence = float(self.pause_confidence)
	self.speaker = int(self.speaker)
	self.speaker_confidence = float(self.speaker_confidence)
	self.words = [word.normalized() for word in self.words]
	return self