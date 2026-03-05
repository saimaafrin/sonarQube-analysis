def popitem(self):
    """
    Remove and return the (key, value) pair most recently used.
    """
    if not self._order:
        raise KeyError("popitem from an empty dictionary")
    key, value = self._order[-1]
    del self._order[-1]
    del self._mapping[key]
    return key, value