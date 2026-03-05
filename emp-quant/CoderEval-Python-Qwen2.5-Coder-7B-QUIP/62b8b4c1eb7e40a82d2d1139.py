def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    return isinstance(candidate, iface) or (not tentative and not isinstance(candidate, iface))