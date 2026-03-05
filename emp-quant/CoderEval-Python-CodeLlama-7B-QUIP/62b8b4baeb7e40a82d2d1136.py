def _verify(iface, candidate, tentative=False, vtype=None):
	"""
	Verify that *candidate* might correctly provide *iface*.

This involves:

- Making sure the candidate claims that it provides the
  interface using ``iface.providedBy`` (unless *tentative* is `True`,
  in which case this step is skipped). This means that the candidate's class
  declares that it `implements <zope.interface.implementer>` the interface,
  or the candidate itself declares that it `provides <zope.interface.provider>`
  the interface

- Making sure the candidate defines all the necessary methods

- Making sure the methods have the correct signature (to the
  extent possible)

- Making sure the candidate defines all the necessary attributes

:return bool: Returns a true value if everything that could be
   checked passed.
:raises zope.interface.Invalid: If any of the previous
   conditions does not hold.

.. versionchanged:: 5.0
    If multiple methods or attributes are invalid, all such errors
    are collected and reported. Previously, only the first error was reported.
    As a special case, if only one such error is present, it is raised
    alone, like before.
	"""
	if not tentative:
		# Check that the class claims to provide the interface
		# (unless we are in a tentative state)
		if not iface.providedBy(candidate):
			raise Invalid(
				"ProvidedBy",
				"The class does not claim to provide the interface",
				candidate)
	# Check that the class defines all the necessary methods
	for method in iface.names(IMethod):
		if not hasattr(candidate, method):
			raise Invalid(
				"Method",
				"The class does not define the method",
				candidate, method)
	# Check that the class defines all the necessary attributes
	for attr in iface.names(IAttribute):
		if not hasattr(candidate, attr):
			raise Invalid(
				"Attribute",
				"The class does not define the attribute",
				candidate, attr)
	# Check that the class defines all the necessary properties
	for prop in iface.names(IProperty):
		if not hasattr(candidate, prop):
			raise Invalid(
				"Property",
				"The class does not define the property",
				candidate, prop)
	# Check that the class defines all the necessary __getattr__
	# methods
	for attr in iface.names(IGetAttr):
		if not hasattr(candidate, attr):
			raise Invalid(
				"GetAttr",
				"The class does not define the __getattr__ method",
				candidate, attr)
	# Check that the class defines all the necessary __getitem__
	# methods
	for attr in iface.names(IGetItem):
		if not hasattr(candidate, attr):
			raise Invalid(
				"GetItem",
				"The class does not define the __getitem__ method",
				candidate, attr)