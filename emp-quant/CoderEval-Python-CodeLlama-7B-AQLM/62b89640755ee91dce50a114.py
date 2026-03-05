def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if sys.version_info[0] == 2:
		def tzname_in_python2_wrapper(self):
			return namefunc(self).encode('ascii')
		return tzname_in_python2_wrapper
	else:
		return namefunc