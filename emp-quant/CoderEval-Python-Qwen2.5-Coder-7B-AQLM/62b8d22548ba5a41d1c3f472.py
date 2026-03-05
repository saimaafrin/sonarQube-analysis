def cachedmethod(cache, key=hashkey, lock=None):
    """
    Returns a decorator function that can call a result in the cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(func, args, kwargs)
            if cache_key in cache:
                return cache[cache_key]
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
        return wrapper
    return decorator