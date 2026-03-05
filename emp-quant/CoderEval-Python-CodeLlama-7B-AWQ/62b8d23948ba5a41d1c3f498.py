def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	# the underlying dict
	cache = {}
	# the order of use
	recency = []
	# the maximum number of items we're willing to keep in the cache
	maxsize = maxsize
	# the number of items we've seen
	hits = misses = 0

	def wrapper(*args):
		# if we've seen this exact sequence of arguments before, just
		# return the value we've seen before
		key = args if typed else tuple(args)
		if key in cache:
			value = cache[key]
			hits += 1
			# move this key to the front of the queue
			recency.remove(key)
			recency.append(key)
			return value
		# if we're at maxsize and we've seen too many items, start
		# discarding the least recently used items
		if len(cache) == maxsize:
			# the key we're about to replace
			oldest = recency.pop(0)
			# if the key we're about to replace hasn't been seen before,
			# we need to subtract from the count of misses
			if oldest not in cache:
				misses -= 1
			del cache[oldest]
		# add the key to the cache and move it to the front
		cache[key] = value = func(*args)
		recency.append(key)
		# if we've seen this exact sequence of arguments before, we only
		# want to count it once
		if key in cache:
			hits += 1
		else:
			misses += 1
		return value

	wrapper.hits = hits
	wrapper.misses = misses
	wrapper.cache_info = lambda: (hits, misses, maxsize, len(cache))
	return wrapper