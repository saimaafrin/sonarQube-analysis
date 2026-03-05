def popitem(self):
    """
    Remove and return the (key, value) pair least frequently used.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    key, value = self._list.popleft()
    del self._data[key]
    return key, value