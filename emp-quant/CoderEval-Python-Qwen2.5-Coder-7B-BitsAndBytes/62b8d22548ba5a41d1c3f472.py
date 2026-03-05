from functools import wraps

def cachedmethod(cache, key=hash, lock=None):
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            cache_key = key((self,) + args, **kwargs)
            if cache_key not in cache:
                with (lock or _NO_LOCK):
                    if cache_key not in cache:
                        cache[cache_key] = method(self, *args, **kwargs)
            return cache[cache_key]
        return wrapper
    return decorator