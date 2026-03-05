def names(self, all=False):
    """
    Return the attribute names of current class.
    """
    if all:
        return [name for name in dir(self) if not name.startswith('__')]
    else:
        return [name for name in dir(self) if not name.startswith('__') and not callable(getattr(self, name))]