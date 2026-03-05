def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Your implementation here
            return func(*args, **kwargs)
        return wrapper
    return decorator