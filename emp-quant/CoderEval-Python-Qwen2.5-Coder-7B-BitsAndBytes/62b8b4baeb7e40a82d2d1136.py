import zope.interface
from zope.interface import Interface, implementer, provider, Invalid

def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative:
        if not iface.providedBy(candidate):
            raise Invalid(f"{candidate} does not claim to provide {iface}")

    implemented_methods = set()
    for method_name in iface.names():
        method = getattr(candidate, method_name, None)
        if method is None:
            raise Invalid(f"{candidate} does not define method {method_name}")
        implemented_methods.add(method_name)

    required_attributes = set(iface.attributes())
    for attr_name in required_attributes:
        if not hasattr(candidate, attr_name):
            raise Invalid(f"{candidate} does not define attribute {attr_name}")

    return True