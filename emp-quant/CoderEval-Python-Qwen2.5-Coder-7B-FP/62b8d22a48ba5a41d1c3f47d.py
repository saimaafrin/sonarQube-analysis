def pop(self, key, default=__marker):
# <editor-fold desc="Docstring">
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	# </editor-fold>
	if key in self:
		value = self[key]
		del self[key]
		return value
	elif default is __marker:
		raise KeyError(key)
	else:
		return default