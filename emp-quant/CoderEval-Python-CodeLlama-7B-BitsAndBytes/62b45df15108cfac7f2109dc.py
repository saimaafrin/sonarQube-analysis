def status_str(self, prefix=''):
	"""
	Return a string with visiting the sorted self.messages list, each visit add prefix and the element in the sorted self.messages list.
	"""
	return prefix + ''.join(map(lambda x: x + '\n', self.messages))