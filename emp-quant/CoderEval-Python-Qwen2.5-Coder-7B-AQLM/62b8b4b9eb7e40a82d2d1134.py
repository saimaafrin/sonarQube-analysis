def namesAndDescriptions(self, all=False):
    """
    Returns the name and description of the current class attribute.
    """
    if all:
        return [(name, attr.__doc__) for name, attr in self.__class__.__dict__.items() if callable(attr)]
    else:
        return [(self.__class__.__name__, self.__class__.__doc__)]