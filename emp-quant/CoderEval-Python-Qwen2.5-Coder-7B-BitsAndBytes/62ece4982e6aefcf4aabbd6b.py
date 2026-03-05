def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    result = set()
    for subclass in cls.__subclasses__():
        result.add(subclass)
        result.update(subclasses(subclass))
    return result