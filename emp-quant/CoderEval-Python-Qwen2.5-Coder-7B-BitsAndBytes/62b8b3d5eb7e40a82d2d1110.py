try:
    from . import c_optimizations
    return c_optimizations
except ImportError:
    return None