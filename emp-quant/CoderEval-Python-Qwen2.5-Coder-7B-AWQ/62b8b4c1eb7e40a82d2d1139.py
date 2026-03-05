import inspect

def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if not tentative:
        return issubclass(candidate, iface)
    
    return all(hasattr(candidate, attr) for attr in dir(iface))