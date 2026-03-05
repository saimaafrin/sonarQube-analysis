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
		iface.providedBy(candidate)

	# Check that all required methods are present
	for method in iface.getMethodNames():
		if not hasattr(candidate, method):
			raise Invalid("Missing method %s" % (method,))

	# Check that all required attributes are present
	for attr in iface.getAttributeNames():
		if not hasattr(candidate, attr):
			raise Invalid("Missing attribute %s" % (attr,))

	# Check that all required methods have the correct signature
	for method in iface.getMethodNames():
		iface_method = getattr(iface, method)
		candidate_method = getattr(candidate, method)
		if not _verify_method(iface_method, candidate_method, vtype):
			raise Invalid("Method %s has wrong signature" % (method,))

	return True