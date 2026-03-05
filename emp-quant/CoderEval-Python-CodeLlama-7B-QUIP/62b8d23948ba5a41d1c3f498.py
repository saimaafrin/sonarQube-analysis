def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorate(obj):
		if maxsize <= 0:
			return obj
		if typed:
			class Wrapper(obj):
				def __call__(self, *args):
					return obj.__call__(self, args)
				def __get__(self, instance):
					return obj.__get__(instance, self)
			return Wrapper(obj)
		def wrapper(*args):
			if maxsize <= 0:
				return obj(*args)
			if typed:
				args = args[0]
			if args in wrapper.cache:
				return wrapper.cache[args]
			wrapper.cache[args] = result = obj(*args)
			if len(wrapper.cache) > maxsize:
				result = wrapper.evict()
				if result:
					del wrapper.cache[args]
			return result
		wrapper.cache = {}
		wrapper.evict = lambda: None
		return wrapper
	return decorate