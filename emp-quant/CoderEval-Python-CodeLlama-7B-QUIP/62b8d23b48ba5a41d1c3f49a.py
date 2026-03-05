def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorate(func):
		def wrapper(*args):
			if typed:
				wrapper.cache[str(args)] = wrapper.cache[str(args)]
			else:
				wrapper.cache[str(args)] = wrapper.cache[str(args)]
			return wrapper.cache[str(args)]
		wrapper.cache = {}
		return wrapper
	return decorate