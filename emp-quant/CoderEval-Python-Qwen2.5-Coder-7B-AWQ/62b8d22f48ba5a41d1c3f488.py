def popitem(self):
    if not self:
        raise KeyError("popitem from empty dictionary")
    key = next(iter(self))
    value = self.pop(key)
    return (key, value)