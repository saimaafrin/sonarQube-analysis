def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorator(func):
		class LRUCache(typed):
			def __init__(self, maxsize, ttl, timer):
				self.maxsize = maxsize
				self.ttl = ttl
				self.timer = timer
				self.cache = {}
				self.queue = []
			def __len__(self):
				return len(self.queue)
			def __getitem__(self, key):
				return self.cache[key]
			def __setitem__(self, key, value):
				self.cache[key] = value
				self.queue.append(key)
				while len(self.queue) > self.maxsize:
					key = self.queue.pop(0)
					del self.cache[key]
			def __delitem__(self, key):
				del self.cache[key]
				self.queue.remove(key)
			def __iter__(self):
				return iter(self.queue)
			def __contains__(self, key):
				return key in self.cache
			def __call__(self, *args):
				return func(*args)
			def __repr__(self):
				return repr(self.cache)
			def __str__(self):
				return str(self.cache)
			def __eq__(self, other):
				return self.cache == other.cache
			def __ne__(self, other):
				return self.cache != other.cache
			def __lt__(self, other):
				return self.cache < other.cache
			def __le__(self, other):
				return self.cache <= other.cache
			def __gt__(self, other):
				return self.cache > other.cache
			def __ge__(self, other):