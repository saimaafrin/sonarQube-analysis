def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	class TTLCache(dict):
		def __init__(self, maxsize, ttl, timer):
			self.maxsize = maxsize
			self.ttl = ttl
			self.timer = timer
			self.queue = []

		def __getitem__(self, key):
			item = dict.__getitem__(self, key)
			self.queue.remove(item)
			self.queue.append(item)
			return item[1]

		def __setitem__(self, key, value):
			if key in self:
				del self[key]
			while len(self) >= self.maxsize:
				self.popitem()
			item = self.queue.append((self.timer() + self.ttl, key, value))
			dict.__setitem__(self, key, item)

		def __delitem__(self, key):
			dict.__delitem__(self, key)
			self.queue.remove(self[key])

		def popitem(self):
			if not self.queue:
				raise KeyError
			key = self.queue[0][1]
			del self[key]
			return key, self[key]

	def wrapper(func):
		cache = TTLCache(maxsize, ttl, timer)
		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = (args, tuple(sorted(kwargs.items())))
			if typed:
				key = (key, type(args[0]))
			try:
				return cache[key]
			except KeyError:
				value = func(*args, **kwargs)
				cache[key] = value
				return value
		return wrapped
	return wrapper