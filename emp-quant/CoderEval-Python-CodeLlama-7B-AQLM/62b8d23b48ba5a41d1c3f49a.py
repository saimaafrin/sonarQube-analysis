def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	if maxsize <= 0:
		raise ValueError("maxsize must be a positive integer")

	cache = OrderedDict()

	def decorating_function(*args, **kwargs):
		key = args if typed else (args, frozenset(kwargs.items()))
		try:
			value = cache.pop(key)
		except KeyError:
			if len(cache) >= maxsize:
				cache.popitem(last=False)
			value = func(*args, **kwargs)
			cache[key] = value
		return value

	def clear():
		cache.clear()

	def get(key, default=None):
		try:
			return cache[key]
		except KeyError:
			return default

	def keys():
		return cache.keys()

	def popitem():
		return cache.popitem()

	def setdefault(key, default=None):
		try:
			return cache[key]
		except KeyError:
			cache[key] = default
			return default

	def update(d):
		for key, value in d.items():
			cache[key] = value

	 def __repr__(self):
		return f"{self.__class__.__name__}({maxsize})"

	 def __len__(self):
		return len(cache)

	 def __iter__(self):
		return iter(cache)

	 def __contains__(self, key):
		return key in cache

	 def __getitem__(self, key):
		return cache[key]

	 def __setitem__(self, key, value):
		cache[key] = value

	 def __delitem__(self, key):
		del cache[key]

	 def __reversed__(self):
		return reversed(cache)

	 def __eq__(self, other):
		return dict(self) == other

	 def __le__(self, other):
		return dict(self)