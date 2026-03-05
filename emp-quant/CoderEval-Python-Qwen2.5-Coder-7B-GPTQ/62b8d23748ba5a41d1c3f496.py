from collections import OrderedDict

class LFUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = OrderedDict()
        self.frequency = {}
        self.count = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, tuple(kwargs.items()))
            if key in self.cache:
                self.frequency[key] += 1
                return self.cache[key]
            elif len(self.cache) >= self.maxsize:
                least_frequent_key = min(self.frequency, key=self.frequency.get)
                del self.cache[least_frequent_key]
                del self.frequency[least_frequent_key]
            result = func(*args, **kwargs)
            self.cache[key] = result
            self.frequency[key] = 1
            return result
        return wrapper

lfu_cache = LFUCache