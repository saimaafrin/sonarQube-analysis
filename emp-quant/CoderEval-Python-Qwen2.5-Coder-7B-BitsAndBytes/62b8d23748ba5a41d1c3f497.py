def popitem(self):
    """
    Remove and return the `(key, value)` pair least frequently used.
    """
    if not self:
        raise KeyError('popitem(): dictionary is empty')
    
    key, value = self.most_common(1)[0]
    del self[key]
    return (key, value)