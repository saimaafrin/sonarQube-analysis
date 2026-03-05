import zope.interface

def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative:
        if not iface.providedBy(candidate):
            raise zope.interface.Invalid(f"{candidate} does not claim to provide {iface}")

    missing_methods = [method for method in iface.names() if not hasattr(candidate, method)]
    if missing_methods:
        raise zope.interface.Invalid(f"Missing methods: {', '.join(missing_methods)}")

    # Additional checks can be added here for method signatures and attribute definitions

    return True