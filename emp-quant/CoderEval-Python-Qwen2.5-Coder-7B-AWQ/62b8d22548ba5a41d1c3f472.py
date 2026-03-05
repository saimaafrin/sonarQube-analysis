from functools import wraps

def cachedmethod(cache, key=hashkey, lock=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            with lock or nullcontext():
                result = func(self, *args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator