from functools import wraps
from collections import OrderedDict

class LRUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = OrderedDict()
        self.keys = set()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, frozenset(kwargs.items()))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            elif len(self.cache) >= self.maxsize:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
                self.keys.remove(oldest_key)
            result = func(*args, **kwargs)
            self.cache[key] = result
            self.keys.add(key)
            return result
        return wrapper

lru_cache = lru_cache