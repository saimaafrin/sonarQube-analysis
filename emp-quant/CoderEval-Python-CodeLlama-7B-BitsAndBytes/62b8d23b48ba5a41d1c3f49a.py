def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
			cache = OrderedDict()
		hits = [0]
		misses = [0]
		typed = typed and type(user_function) in (FunctionType, MethodType)
		lock = RLock()
		if typed:
			user_function = cast_self(user_function)
		def wrapper(*args):
			with lock:
				key = args if typed else tuple(args)
				if key in cache:
					hits[0] += 1
					value = cache.pop(key)
				else:
					misses[0] += 1
					if len(cache) == maxsize:
						cache.popitem(last=False)
					value = user_function(*args)
					cache[key] = value
			return value
		wrapper.cache = cache
		wrapper.hits = hits
		wrapper.misses = misses
		wrapper.maxsize = maxsize
		wrapper.cache_info = lambda: CacheInfo(hits[0], misses[0], maxsize, len(cache))
		return wrapper
	return decorating_function