def cachedmethod(cache, key=hash, lock=None):
    """
    Returns a decorator function that can call a result in the cache.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if lock is None:
                lock = threading.Lock()
            key_value = key(self, *args, **kwargs)
            if key_value not in cache:
                with lock:
                    cache[key_value] = func(self, *args, **kwargs)
            return cache[key_value]
        return wrapper
    return decorator