from zope.interface import implementer, provider, Interface, Attribute, Invalid

def verifyObject(iface, candidate, tentative=False):
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"{candidate.__class__} does not provide {iface.__name__}")

    for method_name in iface.getMethods():
        method = getattr(candidate, method_name, None)
        if not method:
            raise Invalid(f"{candidate.__class__} does not define {method_name}")

    for attr_name in iface.getAttributes():
        if not hasattr(candidate, attr_name):
            raise Invalid(f"{candidate.__class__} does not define {attr_name}")

    return True