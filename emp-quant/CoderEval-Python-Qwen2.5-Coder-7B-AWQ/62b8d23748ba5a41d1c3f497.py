def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    key, value = min(self.items(), key=lambda item: item[1])
    del self[key]
    return (key, value)