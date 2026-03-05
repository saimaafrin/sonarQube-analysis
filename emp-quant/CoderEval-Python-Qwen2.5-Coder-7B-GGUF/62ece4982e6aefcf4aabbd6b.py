def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    return set(cls.__subclasses__()).union(
        {s for c in cls.__subclasses__() for s in subclasses(c)})