from zope.interface import implementer, provider, Interface, Invalid, getInterface

def _verify(iface, candidate, tentative=False, vtype=None):
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"Candidate does not claim to provide interface {iface}")

    methods = iface.names()
    attributes = iface.attributes()

    missing_methods = [method for method in methods if not hasattr(candidate, method)]
    missing_attributes = [attr for attr in attributes if not hasattr(candidate, attr)]

    if missing_methods or missing_attributes:
        errors = []
        if missing_methods:
            errors.append(f"Missing methods: {', '.join(missing_methods)}")
        if missing_attributes:
            errors.append(f"Missing attributes: {', '.join(missing_attributes)}")
        raise Invalid('\n'.join(errors))

    return True