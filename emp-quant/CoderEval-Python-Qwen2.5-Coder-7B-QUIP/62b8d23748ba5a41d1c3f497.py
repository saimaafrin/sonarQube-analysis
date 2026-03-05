def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self._mapping:
        raise KeyError("popitem from an empty dictionary")
    key, value = self._mapping.popitem()
    return key, value