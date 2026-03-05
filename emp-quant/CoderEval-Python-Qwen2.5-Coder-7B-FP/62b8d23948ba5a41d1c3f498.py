def lru_cache(maxsize=128, typed=False):
# Import the necessary modules
	from functools import wraps
	from collections import OrderedDict

	# Define the cache wrapper class
	class LRUCache:
		def __init__(self, maxsize, typed):
			self.maxsize = maxsize
			self.typed = typed
			self.cache = OrderedDict()

		def __call__(self, func):
			@wraps(func)
			def wrapper(*args, **kwargs):
				key = args if not self.typed else (func, args, frozenset(kwargs.items()))
				if key in self.cache:
					self.cache.move_to_end(key)
				elif len(self.cache) >= self.maxsize:
					self.cache.popitem(last=False)
				result = func(*args, **kwargs)
				self.cache[key] = result
				return result
			return wrapper

	# Return an instance of the cache wrapper class
	return LRUCache(maxsize, typed)