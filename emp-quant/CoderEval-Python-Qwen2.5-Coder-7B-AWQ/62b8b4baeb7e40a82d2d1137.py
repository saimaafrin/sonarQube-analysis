import zope.interface

def verifyObject(iface, candidate, tentative=False):
    if not tentative:
        if not iface.providedBy(candidate):
            raise zope.interface.Invalid(f"{candidate} does not claim to provide {iface}")

    missing_methods = [method for method in iface.names() if not hasattr(candidate, method)]
    if missing_methods:
        raise zope.interface.Invalid(f"Missing methods: {', '.join(missing_methods)}")

    # Check method signatures (not implemented here)
    # Check attributes (not implemented here)

    return True