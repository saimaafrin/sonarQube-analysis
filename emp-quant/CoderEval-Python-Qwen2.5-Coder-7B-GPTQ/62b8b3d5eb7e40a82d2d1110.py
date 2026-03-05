try:
    from . import _c_optimizations
except ImportError:
    _c_optimizations = None

def _c_optimizations_available():
    """
    If available, return the C optimization module, otherwise a false value.
    """
    return _c_optimizations is not None