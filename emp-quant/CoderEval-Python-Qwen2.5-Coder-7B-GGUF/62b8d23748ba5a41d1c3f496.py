from collections import OrderedDict

class LFUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = OrderedDict()
        self.frequency = {}
        self.size = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = (func, args, tuple(kwargs.items())) if self.typed else (func, args)
            if key in self.cache:
                self.frequency[key] += 1
                self.cache.move_to_end(key)
                return self.cache[key]
            else:
                result = func(*args, **kwargs)
                if self.size >= self.maxsize:
                    lfu_key = min(self.frequency, key=self.frequency.get)
                    del self.cache[lfu_key]
                    del self.frequency[lfu_key]
                    self.size -= 1
                self.cache[key] = result
                self.frequency[key] = 1
                self.size += 1
                return result
        return wrapper

def lfu_cache(maxsize=128, typed=False):
    return LFUCache(maxsize, typed)