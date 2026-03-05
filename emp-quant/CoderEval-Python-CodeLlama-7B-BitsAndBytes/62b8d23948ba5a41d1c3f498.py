def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
			cache = OrderedDict()
		hits = misses = 0
		
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			# Make sure that if we have a typed function we don't
			# accidentally stash an unhashable type in the cache.
			if typed and (not all(isinstance(a, Hashable) for a in args) or
						 not all(isinstance(k, Hashable) for k in kwargs)):
				# Force recomputation.
				pass
			key = args
			if kwargs:
				key += tuple(sorted(kwargs.items()))
			if key in cache:
				hits += 1
				value = cache.pop(key)
			else:
				misses += 1
				value = user_function(*args, **kwargs)
				if len(cache) >= maxsize:
					# Remove the least recently used cache entry.
					# This implementation is inefficient, but it works.
					lru_key = next(iter(cache))
					del cache[lru_key]
				cache[key] = value
			return value
		wrapper.cache = cache
		wrapper.hits = hits
		wrapper.misses = misses
		wrapper.maxsize = maxsize
		return wrapper
	return decorating_function