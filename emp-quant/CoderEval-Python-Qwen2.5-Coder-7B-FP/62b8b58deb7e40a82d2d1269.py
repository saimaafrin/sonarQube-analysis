def directlyProvidedBy(object):
# XXX: This function should be in zope.interface, but it's not.
	return object.__provides__