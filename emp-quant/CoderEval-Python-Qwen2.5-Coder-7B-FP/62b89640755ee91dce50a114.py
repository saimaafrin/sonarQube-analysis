def tzname_in_python2(namefunc):
# Check if the function is already defined
	if namefunc.__name__ == 'tzname':
		return namefunc

	def wrapper():
		result = namefunc()
		if isinstance(result, tuple) and all(isinstance(item, unicode) for item in result):
			return tuple(item.encode('utf-8') for item in result)
		else:
			return result

	wrapper.__name__ = namefunc.__name__
	return wrapper