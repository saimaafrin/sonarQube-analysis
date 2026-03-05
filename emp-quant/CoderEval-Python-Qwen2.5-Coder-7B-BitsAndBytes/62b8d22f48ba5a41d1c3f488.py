def popitem(self):
    """
    Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
    """
    if not self:
        raise KeyError("popitem(): dictionary is empty")
    
    first_key = next(iter(self))
    value = self.pop(first_key)
    return (first_key, value)