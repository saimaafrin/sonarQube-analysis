def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
			cache = _LFUCache(maxsize, typed, user_function)
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = _make_key(args, kwargs, typed, user_function)
			if key in cache:
				#print("cache hit")
				#print(cache[key])
				#print(cache.hits)
				#print(cache.misses)
				#print(cache.hits + cache.misses)
				#print(cache.hits / (cache.hits + cache.misses))
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)
				#print(cache.hits / (cache.hits + cache.misses) * 100)