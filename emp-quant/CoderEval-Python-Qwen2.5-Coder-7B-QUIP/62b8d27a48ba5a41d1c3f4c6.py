def cached(cache, key=hash, lock=None):
    """
    Returns a decorator function that saves the results in the cache
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if lock is None:
                lock = threading.Lock()
            key_value = key(*args, **kwargs)
            if key_value not in cache:
                with lock:
                    cache[key_value] = func(*args, **kwargs)
            return cache[key_value]
        return wrapper
    return decorator