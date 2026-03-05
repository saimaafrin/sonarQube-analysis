import inspect

def names(self, all=False):
    """
    Return the attribute names of current class.
    """
    if all:
        return [name for name in dir(self) if not name.startswith('__')]
    else:
        return [name for name in dir(self) if not (name.startswith('__') or callable(getattr(self, name)))]