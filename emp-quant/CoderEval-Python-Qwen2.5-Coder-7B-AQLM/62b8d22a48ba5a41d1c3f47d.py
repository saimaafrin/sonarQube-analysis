class Dict:
    def __init__(self):
        self._data = {}

    def pop(self, key, default=None):
        if key in self._data:
            value = self._data[key]
            del self._data[key]
            return value
        elif default is not None:
            return default
        else:
            raise KeyError(key)