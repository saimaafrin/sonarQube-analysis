from functools import wraps

def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    def decorator(func):
        cache = {}
        recent_keys = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values()) if not typed else args + tuple(map(type, args)) + tuple(kwargs.values())
            if key in cache:
                recent_keys.remove(key)
                recent_keys.append(key)
                return cache[key]
            elif len(cache) >= maxsize:
                oldest_key = recent_keys.pop(0)
                del cache[oldest_key]
            result = func(*args, **kwargs)
            cache[key] = result
            recent_keys.append(key)
            return result

        return wrapper

    return decorator