import zope.interface
from zope.interface import Interface, implementer, provider

def verifyObject(iface, candidate, tentative=False):
    if not tentative and not iface.providedBy(candidate):
        raise zope.interface.Invalid(f"{candidate} does not claim to provide {iface}")

    methods = iface.__dict__.get('__methods__', [])
    attributes = iface.__dict__.get('__attributes__', [])

    for method in methods:
        if not hasattr(candidate, method):
            raise zope.interface.Invalid(f"{candidate} does not define method {method}")
        method_obj = getattr(candidate, method)
        if not callable(method_obj):
            raise zope.interface.Invalid(f"{method} in {candidate} is not callable")

    for attribute in attributes:
        if not hasattr(candidate, attribute):
            raise zope.interface.Invalid(f"{candidate} does not define attribute {attribute}")

    return True