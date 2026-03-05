def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	if maxsize <= 0:
		raise ValueError("maxsize must be positive")

	cache = {}
	hits = {}
	misses = {}
	full = False
	lock = RLock()

	def wrapper(*args, **kwds):
		# cache_key = _make_key(args, kwds, typed)
		cache_key = args
		with lock:
			if cache_key in cache:
				# Move the item to the front of the list
				del cache[cache_key]
				cache[cache_key] = cache.pop(cache_key)
				hits[cache_key] = hits.get(cache_key, 0) + 1
				return cache[cache_key]
			if full:
				# Make room for the new item by removing the least frequently used
				# cache item
				lfu_items = list(hits.items())
				lfu_items.sort(key=lambda x: x[1])
				for cache_key, _ in lfu_items[:1]:
					del cache[cache_key]
					del hits[cache_key]
					del misses[cache_key]
			misses[cache_key] = misses.get(cache_key, 0) + 1
			result = user_function(*args, **kwds)
			cache[cache_key] = result
			hits[cache_key] = hits.get(cache_key, 0) + 1
			if len(cache) == maxsize:
				full = True
			return result

	def cache_info():
		"""Report cache statistics"""
		with lock:
			return _CacheInfo(hits, misses, maxsize, len(cache))

	def cache_clear():
		"""Clear the cache and cache statistics"""
		with lock:
			cache.clear()