def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    return self._OrderedDict__map.popitem(last=False)