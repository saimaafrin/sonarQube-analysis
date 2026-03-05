import time
from functools import wraps
from collections import OrderedDict

class TTLCache:
    def __init__(self, maxsize, ttl, timer, typed):
        self.cache = OrderedDict()
        self.maxsize = maxsize
        self.ttl = ttl
        self.timer = timer
        self.typed = typed

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (func, args, tuple(kwargs.items())) if self.typed else (func, args, frozenset(kwargs.items()))
            now = self.timer()
            if key in self.cache:
                if now - self.cache[key][1] < self.ttl:
                    return self.cache[key][0]
                else:
                    del self.cache[key]
            if len(self.cache) >= self.maxsize:
                self.cache.popitem(last=False)
            result = func(*args, **kwargs)
            self.cache[key] = (result, now)
            return result
        return wrapper

ttl_cache = TTLCache