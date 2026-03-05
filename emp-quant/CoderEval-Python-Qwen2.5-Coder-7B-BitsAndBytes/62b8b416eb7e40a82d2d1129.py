import inspect

def names(self, all=False):
    """
    Return the attribute names of current class.
    """
    if all:
        return [name for name, value in inspect.getmembers(self.__class__) if not name.startswith('__')]
    else:
        return [name for name, value in inspect.getmembers(self) if not name.startswith('__')]