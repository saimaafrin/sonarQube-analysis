def subclasses(cls):
    result = set()
    for subclass in cls.__subclasses__():
        result.add(subclass)
        result.update(subclasses(subclass))
    return result