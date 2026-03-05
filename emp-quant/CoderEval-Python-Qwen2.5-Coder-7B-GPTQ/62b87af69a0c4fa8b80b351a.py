def is_fill_compute_el(obj):
    return hasattr(obj, 'fill') and callable(obj.fill) and \
           hasattr(obj, 'compute') and callable(obj.compute)