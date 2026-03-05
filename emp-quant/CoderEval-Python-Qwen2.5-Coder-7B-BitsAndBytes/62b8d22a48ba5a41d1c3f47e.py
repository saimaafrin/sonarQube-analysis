if key in self.__dict__:
    return self.__dict__[key]
else:
    self.__dict__[key] = default
    return default