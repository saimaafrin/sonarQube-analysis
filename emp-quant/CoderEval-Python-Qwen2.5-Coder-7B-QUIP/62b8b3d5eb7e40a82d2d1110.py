try:
    from .c_optimizations import c_optimizations
    return c_optimizations
except ImportError:
    return False