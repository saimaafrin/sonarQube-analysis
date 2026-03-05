from zope.interface.interfaces import IInterface

def directlyProvidedBy(object):
    return IInterface.get(object, None)