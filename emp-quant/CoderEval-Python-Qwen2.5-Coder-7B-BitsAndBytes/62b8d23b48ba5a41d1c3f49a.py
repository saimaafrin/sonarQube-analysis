from functools import wraps

class MRUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = {}
        self.order = []

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, frozenset(kwargs.items()))
            if key in self.cache:
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.maxsize:
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = result
            self.order.append(key)
            return result
        return wrapper

mru_cache = MRUCache