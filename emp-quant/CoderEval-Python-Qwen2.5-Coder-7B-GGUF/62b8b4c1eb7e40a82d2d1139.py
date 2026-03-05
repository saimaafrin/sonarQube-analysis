def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if tentative:
        return iface in candidate.__dict__
    else:
        return all(hasattr(candidate, attr) for attr in iface.__dict__)