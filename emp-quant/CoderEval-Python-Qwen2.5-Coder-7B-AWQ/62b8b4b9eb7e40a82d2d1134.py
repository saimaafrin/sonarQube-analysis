def namesAndDescriptions(self, all=False):
    """
    Returns the name and description of the current class attribute.
    """
    if all:
        return {attr: getattr(self, attr).__doc__ for attr in dir(self) if callable(getattr(self, attr))}
    else:
        return {self.__class__.__name__: self.__doc__}