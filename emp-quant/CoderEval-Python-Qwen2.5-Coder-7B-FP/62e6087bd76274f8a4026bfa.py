def pop_u16(self):
# BEGIN SOLUTION
	return self.data.pop() + (self.data.pop() << 8)
	# END SOLUTION