from functools import wraps
from collections import OrderedDict

def mru_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = OrderedDict()
        hit = miss = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args if not typed else (args, tuple(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
                nonlocal hit
                hit += 1
                return cache[key]
            else:
                nonlocal miss
                miss += 1
                result = func(*args, **kwargs)
                cache[key] = result
                if len(cache) > maxsize:
                    cache.popitem(last=False)
                return result

        wrapper.cache_info = lambda: (hit, miss, len(cache), maxsize)
        return wrapper

    return decorator