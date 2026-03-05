from functools import wraps

def cached(cache, key=None, lock=None):
    if key is None:
        def default_key(func, *args, **kwargs):
            return hash((func.__name__, args, tuple(kwargs.items())))
        key = default_key
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key(func, *args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
        return wrapper
    return decorator