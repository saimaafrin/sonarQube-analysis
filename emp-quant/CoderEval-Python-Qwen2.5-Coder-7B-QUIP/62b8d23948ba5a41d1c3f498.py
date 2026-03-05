from functools import wraps

def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values()) if not typed else args + tuple(kwargs.values())
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper
    return decorator