class D:
    __marker = object()

    def __init__(self):
        self._data = {}

    def pop(self, key, default=__marker):
        if key in self._data:
            value = self._data[key]
            del self._data[key]
            return value
        elif default is not self.__marker:
            return default
        else:
            raise KeyError(key)