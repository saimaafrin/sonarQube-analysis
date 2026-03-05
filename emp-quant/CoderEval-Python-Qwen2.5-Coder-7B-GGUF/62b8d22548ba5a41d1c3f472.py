def cachedmethod(cache, key=hashkey, lock=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if lock is not None:
                lock.acquire()
            try:
                cache_key = key(func, args, kwargs)
                if cache_key in cache:
                    return cache[cache_key]
                result = func(*args, **kwargs)
                cache[cache_key] = result
                return result
            finally:
                if lock is not None:
                    lock.release()
        return wrapper
    return decorator