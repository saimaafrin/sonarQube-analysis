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

	def decorating_function(*args, **kwargs):
		with lock:
			key = make_key(args, kwargs, typed)
			result = cache.get(key, _missing)
			if result is not _missing:
				hits[key] = hits.get(key, 0) + 1
				return result
			if full:
				# make room for the new key
				victim_key, victim_value = min(hits.items(), key=itemgetter(1))
				del cache[victim_key]
				del hits[victim_key]
				del misses[victim_key]
			result = func(*args, **kwargs)
			cache[key] = result
			hits[key] = 1
			if key in misses:
				del misses[key]
			if len(cache) == maxsize:
				full = True
			return result

	def cache_info():
		"""Report cache statistics"""
		with lock:
			return len(cache), len(hits), len(misses)

	def cache_clear():
		"""Clear the cache and cache statistics"""
		with lock:
			cache.clear()
			hits.clear()
			misses.clear()
			full = False

	def cache_stats():
		"""Return a human readable version of the cache statistics"""
		with lock:
			hits = sum(hits.values())
			misses = sum(misses.values())
			full = len(cache) == maxsize
			return "Cache size: %d, hits: %d, misses: