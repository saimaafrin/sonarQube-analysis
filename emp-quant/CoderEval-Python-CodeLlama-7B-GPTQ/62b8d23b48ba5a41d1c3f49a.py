def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = OrderedDict()
		hits = [0]

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			# cache_key = args
			# if len(args) == 1 and isinstance(args[0], (list, tuple)):
			# 	cache_key = args[0]
			# elif len(args) == 1 and isinstance(args[0], dict):
			# 	cache_key = tuple(args[0].items())
			# else:
			# 	cache_key = args
			# cache_key = tuple(cache_key)
			# print(cache_key)
			# print(cache)
			# print(cache.keys())
			# print(cache.values())
			# print(cache.items())
			# print(cache.get(cache_key))
			# print(cache.get(cache_key, None))
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_key, None) is not None)
			# print(cache.get(cache_