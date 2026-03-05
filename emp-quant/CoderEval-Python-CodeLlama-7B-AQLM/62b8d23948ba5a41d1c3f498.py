def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	# the order dictionary stores the order in which the keys were last
	# accessed
	class OrderedDict(dict):
		def __init__(self, maxsize=None, *args, **kwds):
			self.maxsize = maxsize
			super(OrderedDict, self).__init__(*args, **kwds)
			self.order = []
		
		def __setitem__(self, key, value):
			if key in self:
				self.order.remove(key)
			elif len(self) >= self.maxsize:
				self.popitem()
			self.order.append(key)
			super(OrderedDict, self).__setitem__(key, value)
		
		def __delitem__(self, key):
			self.order.remove(key)
			super(OrderedDict, self).__delitem__(key)
		
		def __getitem__(self, key):
			self.order.remove(key)
			self.order.append(key)
			return super(OrderedDict, self).__getitem__(key)
		
		def __repr__(self):
			return 'OrderedDict(%r, %r)' % (self.order, super(OrderedDict, self).__repr__())
	
	def decorating_function(user_function):
		cache = OrderedDict(maxsize=maxsize)
		
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = _make_key(args, kwargs, typed, user_function.__name__)
			
			if key not in cache:
				cache[key] = user_function(*args, **kwargs)
			
			return cache[key]
		
		wrapper.cache = cache
		return wrapper
	
	return decorating_function