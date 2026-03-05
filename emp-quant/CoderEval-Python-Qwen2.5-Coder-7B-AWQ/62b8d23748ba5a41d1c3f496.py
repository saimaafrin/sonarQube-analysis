from collections import OrderedDict

class LFUCache:
    def __init__(self, maxsize, typed):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = OrderedDict()
        self.freq = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = args if not self.typed else (func, args, frozenset(kwargs.items()))
            freq_key = key

            if key in self.cache:
                self.freq[freq_key] += 1
                self.cache.move_to_end(key)
            else:
                if len(self.cache) >= self.maxsize:
                    least_freq_key = min(self.freq, key=self.freq.get)
                    del self.cache[least_freq_key]
                    del self.freq[least_freq_key]

                self.cache[key] = func(*args, **kwargs)
                self.freq[freq_key] = 1

            return self.cache[key]
        return wrapper

# Usage example:
@lfu_cache(maxsize=3, typed=True)
def expensive_function(x):
    print(f"Computing {x}")
    return x * x

print(expensive_function(1))  # Computes and caches 1
print(expensive_function(2))  # Computes and caches 4
print(expensive_function(1))  # Retrieves from cache
print(expensive_function(3))  # Computes and caches 9
print(expensive_function(2))  # Retrieves from cache