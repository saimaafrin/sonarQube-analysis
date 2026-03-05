from zope.interface import implementedBy

def directlyProvidedBy(object):
    """
    Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
    return implementedBy(object)