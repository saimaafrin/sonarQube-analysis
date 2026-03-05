from collections import OrderedDict, Counter

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = OrderedDict()
        frequency = Counter()

        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items())) if typed else (args, tuple(sorted(kwargs.items())))
            if key in cache:
                frequency[key] += 1
                cache.move_to_end(key)
            else:
                if len(cache) >= maxsize:
                    lfu_key = min(frequency, key=frequency.get)
                    del cache[lfu_key]
                    del frequency[lfu_key]
                cache[key] = func(*args, **kwargs)
                frequency[key] = 1
            return cache[key]

        return wrapper

    return decorator