from zope.interface import Interface, implementer, provider, Invalid, getInterface
from inspect import getmembers, isfunction, ismethod, signature

def verifyObject(iface, candidate, tentative=False):
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"{candidate} does not claim to provide {iface}")

    candidate_methods = set(getmembers(candidate, predicate=lambda x: isfunction(x) or ismethod(x)))
    required_methods = set(getmembers(iface, predicate=lambda x: isfunction(x) or ismethod(x)))

    if not candidate_methods.issuperset(required_methods):
        missing_methods = required_methods - candidate_methods
        raise Invalid(f"{candidate} is missing methods: {missing_methods}")

    for method_name, method in candidate_methods:
        if method_name in required_methods:
            required_method = getattr(iface, method_name)
            if not signature(required_method).parameters == signature(method).parameters:
                raise Invalid(f"{candidate} method {method_name} has incorrect signature")

    candidate_attributes = set(getmembers(candidate, predicate=lambda x: not (isfunction(x) or ismethod(x))))
    required_attributes = set(getmembers(iface, predicate=lambda x: not (isfunction(x) or ismethod(x))))

    if not candidate_attributes.issuperset(required_attributes):
        missing_attributes = required_attributes - candidate_attributes
        raise Invalid(f"{candidate} is missing attributes: {missing_attributes}")

    return True