def popitem(self):
    """
    Remove and return the (key, value) pair most recently used.
    """
    if not self:
        raise KeyError('popitem(): dictionary is empty')
    key = next(iter(self))
    return (key, self.pop(key))