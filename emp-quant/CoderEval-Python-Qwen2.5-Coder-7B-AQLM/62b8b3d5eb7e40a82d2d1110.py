try:
    import _c_optimizations
    return _c_optimizations
except ImportError:
    return None