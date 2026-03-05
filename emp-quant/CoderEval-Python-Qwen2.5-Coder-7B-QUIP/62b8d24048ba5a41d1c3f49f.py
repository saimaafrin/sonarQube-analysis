from functools import wraps
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values()) if not typed else args + tuple(kwargs.values())
            if key in cache and timer() - cache[key]['timestamp'] <= ttl:
                return cache[key]['value']
            result = func(*args, **kwargs)
            cache[key] = {'value': result, 'timestamp': timer()}
            if len(cache) > maxsize:
                oldest_key = min(cache, key=lambda k: cache[k]['timestamp'])
                del cache[oldest_key]
            return result
        return wrapper
    return decorator