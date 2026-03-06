def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	with self.lock:
		if key in self.d:
			x = self.d[key]
			del self.d[key]
			return x
		elif default is not __marker:
			return default
		else:
			raise KeyError(key)