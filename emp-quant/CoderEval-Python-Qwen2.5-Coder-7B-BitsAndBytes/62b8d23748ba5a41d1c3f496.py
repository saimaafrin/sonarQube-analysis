from collections import OrderedDict

class LFUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = OrderedDict()
        self.usage = {}
        self.keys = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, frozenset(kwargs.items()))
            if key in self.cache:
                self.usage[key] += 1
                return self.cache[key]
            elif len(self.cache) >= self.maxsize:
                least_used_key = min(self.usage, key=self.usage.get)
                del self.cache[least_used_key]
                del self.usage[least_used_key]
                del self.keys[least_used_key]
            result = func(*args, **kwargs)
            self.cache[key] = result
            self.usage[key] = 1
            self.keys[key] = len(self.cache)
            return result
        return wrapper