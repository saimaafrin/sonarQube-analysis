def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	with self.lock:
		if key in self.data:
			value = self.data[key]
			del self.data[key]
			return value
		if default is self.__marker:
			raise KeyError(key)
		return default