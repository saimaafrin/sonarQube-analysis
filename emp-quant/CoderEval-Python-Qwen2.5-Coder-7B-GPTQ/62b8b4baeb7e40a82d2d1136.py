import zope.interface
from zope.interface import implementer, provider, Interface, Invalid

def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative:
        if not iface.providedBy(candidate):
            raise Invalid(f"{candidate} does not claim to provide {iface}")

    missing_methods = [method for method in iface.names() if not hasattr(candidate, method)]
    if missing_methods:
        raise Invalid(f"{candidate} is missing methods: {', '.join(missing_methods)}")

    wrong_signature_methods = []
    for method_name in iface.names():
        method = getattr(candidate, method_name)
        expected_signature = iface.get(method_name).__annotations__
        actual_signature = {}
        try:
            from inspect import getfullargspec
            argspec = getfullargspec(method)
            actual_signature['args'] = argspec.args
            actual_signature['varargs'] = argspec.varargs
            actual_signature['varkw'] = argspec.varkw
            actual_signature['defaults'] = argspec.defaults
        except TypeError:
            pass
        if actual_signature != expected_signature:
            wrong_signature_methods.append((method_name, expected_signature, actual_signature))

    if wrong_signature_methods:
        error_messages = [
            f"{method_name} has incorrect signature: expected {expected}, got {actual}"
            for method_name, expected, actual in wrong_signature_methods
        ]
        raise Invalid(", ".join(error_messages))

    missing_attributes = [attr for attr in iface.names() if not hasattr(candidate, attr)]
    if missing_attributes:
        raise Invalid(f"{candidate} is missing attributes: {', '.join(missing_attributes)}")

    return True