import inspect

def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if not tentative:
        return all(hasattr(candidate, attr) and callable(getattr(candidate, attr)) for attr in iface.__dict__ if not attr.startswith('__'))
    else:
        return all(hasattr(candidate, attr) for attr in iface.__dict__ if not attr.startswith('__'))