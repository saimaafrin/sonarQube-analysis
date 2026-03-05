from functools import wraps
from collections import OrderedDict

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = OrderedDict()
        cache_size = 0
        hit_count = 0
        miss_count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values()) if not typed else args + tuple(kwargs.values())
            if key in cache:
                cache.move_to_end(key)
                hit_count += 1
            else:
                miss_count += 1
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator