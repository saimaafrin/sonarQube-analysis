import time
from functools import wraps, lru_cache

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache = lru_cache(maxsize=maxsize, typed=typed)(func)
            result = cache(*args, **kwargs)
            cache.cache_info = lambda: (cache.cache_info()[0], cache.cache_info()[1], cache.cache_info()[2], cache.cache_info()[3], timer() - cache.cache_info()[4])
            return result
        return wrapper
    return decorator