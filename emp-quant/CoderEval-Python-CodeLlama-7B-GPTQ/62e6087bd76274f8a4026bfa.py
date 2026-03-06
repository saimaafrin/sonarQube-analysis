def pop_u16(self):
	"""
	Remove the last two elements in self.data and return
	"""
	if self.size < 2:
		raise IndexError("pop_u16: stack is too small")
	self.size -= 2
	return self.data[self.size:]