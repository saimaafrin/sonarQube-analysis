def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = {}
		hits = {}
		misses = {}
		full = False
		def wrapped_function(*args, **kwargs):
			key = str(args) + str(kwargs)
			if key not in cache:
				if full:
					# make room by removing the least frequently used cache entry
					lfu_key = lfu_iter(hits).next()
					del cache[lfu_key]
					del hits[lfu_key]
					del misses[lfu_key]
				# then calculate the result
				result = user_function(*args, **kwargs)
				cache[key] = result
				hits[key] = misses.get(key, 0) + 1
				misses[key] = 0
			else:
				result = cache[key]
				hits[key] += 1
				misses[key] = 0
			return result
		def cache_info():
			"""
			Return the number of hits and misses for all arguments.
			"""
			return (sum(hits.values()), sum(misses.values()))
		def clear():
			"""Clear the cache and cache counters."""
			cache.clear()
			hits.clear()
			misses.clear()
			full = False
		wrapped_function.cache_info = cache_info
		wrapped_function.cache_clear = clear
		return wrapped_function
	return decorating_function