def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def tzname_in_python2(namefunc):
		def tzname_in_python2(self):
			name = namefunc(self)
			if isinstance(name, unicode):
				return name.encode('latin1')
			return name
		return tzname_in_python2
	return tzname_in_python2