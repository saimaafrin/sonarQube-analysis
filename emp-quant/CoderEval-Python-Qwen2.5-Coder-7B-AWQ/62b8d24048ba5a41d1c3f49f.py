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
            key = (func, args, tuple(kwargs.items())) if self.typed else (func, tuple(args), tuple(kwargs.items()))
            now = self.timer()
            if key in self.cache:
                entry = self.cache[key]
                if now - entry['time'] < self.ttl:
                    return entry['value']
                del self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.maxsize:
                oldest_key = min(self.cache, key=lambda k: self.cache[k]['time'])
                del self.cache[oldest_key]
            self.cache[key] = {'value': result, 'time': now}
            return result
        return wrapper

ttl_cache = TTLCache