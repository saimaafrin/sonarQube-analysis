def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if sys.version_info[0] < 3:
		def tzname_in_python2(namefunc):
			def tzname(dt):
				return namefunc(dt).encode('ascii')
			return tzname
		return tzname_in_python2(namefunc)
	else:
		return namefunc