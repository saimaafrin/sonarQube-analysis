def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self:
        raise KeyError('popitem(): dictionary is empty')
    
    key, value = self._OrderedDict__map.popitem(last=False)
    del self.__dict__[key]
    return (key, value)