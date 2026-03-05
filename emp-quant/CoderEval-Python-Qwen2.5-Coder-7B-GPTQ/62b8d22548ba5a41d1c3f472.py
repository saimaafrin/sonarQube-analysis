from functools import wraps

def cachedmethod(cache, key=None, lock=None):
    if key is None:
        key = hashkey
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key(args, kwargs)
            if cache_key in cache:
                return cache[cache_key]
            with lock or nullcontext():
                result = func(*args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator