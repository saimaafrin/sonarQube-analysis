def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if tentative:
        return all(hasattr(candidate, attr) for attr in iface.__dict__)
    else:
        return all(getattr(candidate, attr) == getattr(iface, attr) for attr in iface.__dict__)