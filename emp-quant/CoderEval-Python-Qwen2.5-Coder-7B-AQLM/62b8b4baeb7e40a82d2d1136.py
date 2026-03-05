import zope.interface
from zope.interface import Interface, implementer, provider

def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative and not iface.providedBy(candidate):
        raise zope.interface.Invalid(f"Candidate does not claim to provide interface {iface}")

    methods = iface.__dict__.get('__methods__', [])
    attributes = iface.__dict__.get('__attributes__', [])

    for method in methods:
        if not hasattr(candidate, method):
            raise zope.interface.Invalid(f"Candidate does not define method {method}")
        method_obj = getattr(candidate, method)
        if not callable(method_obj):
            raise zope.interface.Invalid(f"Method {method} is not callable")

    for attribute in attributes:
        if not hasattr(candidate, attribute):
            raise zope.interface.Invalid(f"Candidate does not define attribute {attribute}")

    return True