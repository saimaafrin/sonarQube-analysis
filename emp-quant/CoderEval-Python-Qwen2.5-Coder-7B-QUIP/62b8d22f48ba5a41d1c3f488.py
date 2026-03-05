def popitem(self):
    """
    Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
    """
    if self._keys:
        key = self._keys[0]
        value = self._values[0]
        del self._keys[0]
        del self._values[0]
        return key, value
    else:
        raise KeyError("popitem from an empty dictionary")