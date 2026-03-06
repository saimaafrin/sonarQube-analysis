def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if sys.version_info[0] == 2:
		def wrapper(tz):
			return namefunc(tz).encode('ascii')
		return wrapper
	else:
		return namefunc