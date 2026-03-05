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

	def wrapper(*args):
		"""
		If there are any values in the cache, return the one with the
		least frequency. Otherwise, call the decorated function and add
		the result to the cache.
		"""
		with lock:
			key = _make_key(args, kwargs, typed)
			result = cache.get(key, _missing)
			if result is not _missing:
				hits[key] = hits.get(key, 0) + 1
				return result
			result = _call_and_cache(key, *args)
			misses[key] = misses.get(key, 0) + 1
			return result

	def _get_hits(key):
		"""
		Return the number of times the given key has been accessed.
		"""
		with lock:
			return hits.get(key, 0)

	def _get_misses(key):
		"""
		Return the number of times the given key has been missed.
		"""
		with lock:
			return misses.get(key, 0)

	def _set_hits(key, n):
		"""
		Set the number of times the given key has been accessed to `n`.
		"""
		with lock:
			hits[key] = n

	def _set_misses(key, n):
		"""
		Set the number of times the given key has been missed to `n`.
		"""
		with lock:
			misses[key] = n

	def _make_key(*args, **kwargs):
		"""
		Create a key from the given arguments.
		"""
		if typed: