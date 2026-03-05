from functools import wraps

class LRUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = {}
        self.keys = []

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.keys.remove(key)
                self.keys.append(key)
                return self.cache[key]
            result = func(*args, **kwargs)
            self.cache[key] = result
            self.keys.append(key)
            if len(self.cache) > self.maxsize:
                oldest_key = self.keys.pop(0)
                del self.cache[oldest_key]
            return result
        return wrapper

lru_cache = LRUCache