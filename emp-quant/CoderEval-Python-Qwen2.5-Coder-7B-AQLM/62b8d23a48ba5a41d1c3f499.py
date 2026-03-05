def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self:
        raise KeyError('popitem from an empty OrderedDict')
    key, value = self._OrderedDict__map.popitem(last=False)
    del self._OrderedDict__data[key]
    return key, value