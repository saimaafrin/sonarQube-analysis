from inspect import getmro

def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    if explicit_mc is not None:
        return explicit_mc
    for base in bases:
        if hasattr(base, '__metaclass__'):
            return base.__metaclass__
    for cls in getmro(base):
        if hasattr(cls, '__metaclass__'):
            return cls.__metaclass__
    return type