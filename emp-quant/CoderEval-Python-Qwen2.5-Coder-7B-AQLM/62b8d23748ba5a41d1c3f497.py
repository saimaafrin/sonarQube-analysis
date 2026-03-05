def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError("popitem from an empty cache")
    key, value = self._list.popleft()
    del self._cache[key]
    return key, value