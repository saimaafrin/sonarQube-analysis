import time
from functools import wraps

class TTLCache:
    def __init__(self, maxsize, ttl, timer, typed):
        self.cache = {}
        self.maxsize = maxsize
        self.ttl = ttl
        self.timer = timer
        self.typed = typed

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, tuple(kwargs.items()))
            now = self.timer()
            if key in self.cache:
                entry = self.cache[key]
                if entry[1] + entry[2] > now:
                    return entry[0]
                del self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.maxsize:
                oldest_key = min(self.cache, key=lambda k: self.cache[k][1])
                del self.cache[oldest_key]
            self.cache[key] = (result, now, self.ttl)
            return result
        return wrapper

ttl_cache = TTLCache