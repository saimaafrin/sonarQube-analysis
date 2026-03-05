def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self._order:
        raise KeyError("popitem(): dictionary is empty")
    key, value = self._order.popitem(last=True)
    return key, value