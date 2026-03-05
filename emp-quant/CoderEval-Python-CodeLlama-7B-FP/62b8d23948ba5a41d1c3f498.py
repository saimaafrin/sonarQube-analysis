def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	# the underlying dict
	cache = {}
	# the order of use
	recent_keys = []
	# the size of the cache
	size = 0

	def wrapper(*args, **kwds):
		# if we have too many items in the cache,
		# we need to remove the least recently used
		if size > maxsize:
			# we do this in O(1) time by simply
			# popping the first item off the list
			recent_keys.pop(0)
			size -= 1

		# if we have seen this key before, we need
		# to remove it from the list of recent keys
		# so that it can be moved to the end
		if kwds or typed:
			# kwds is a dictionary of keyword arguments
			# so we need to hash it
			key = (args, tuple(sorted(kwds.items())))
		else:
			# if we have no keyword arguments,
			# we can simply hash the positional
			# arguments
			key = args

		# if we have seen this key before,
		# we need to remove it from the list
		# of recent keys so that it can be
		# moved to the end
		if key in cache:
			recent_keys.remove(key)
			size -= 1

		# add the key to the end of the list
		# of recent keys
		recent_keys.append(key)

		# add the key to the cache
		cache[key] = wrapper(*args, **kwds)
		size += 1

		# return the value from the cache
		return cache[key]

	# return the wrapped function
	return wrapper