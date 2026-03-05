def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	# handle unlimited sizes
	if maxsize is None or maxsize < 0:
		return lambda f: f

	# handle infinte sizes
	if maxsize == 0:
		maxsize = None

	# decorator
	def decorating_function(user_function):
		cache = OrderedDict()
		hits = Misses = 0
		wrap = lambda key, result: (key, result)
		getitem = lambda key: cache[key]
		cache_info = lambda: (len(cache), maxsize, hits, Misses)
		make_key = lambda args, kwargs: args
		if typed:
			def make_key(args, kwargs, typed):
				return args, tuple(kwargs.items())
			getitem = lambda key: cache[key[0]][key[1]]
			wrap = lambda key, result: (key[0], key[1], result)
		cache.__getitem__ = getitem
		cache.__len__ = len
		cache.cache_info = cache_info
		cache.cache_clear = lambda: cache.clear()
		def wrapper(*args, **kwargs):
			nonlocal hits, Misses
			key = make_key(args, kwargs, typed)
			result = cache.get(key, _sentinel)
			if result is not _sentinel:
				hits += 1
				return result
			result = user_function(*args, **kwargs)
			cache[key] = result
			return result
		wrapper.__wrapped__ = user_function
		wrapper.cache_info = cache_info
		wrapper.cache_clear = cache.cache_clear
		return update_wrapper(wrapper, user_function)
	return decorating_function