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
	for name, method in iface.namesAndDescriptors():
		if name == '__init__':
			continue
		if not hasattr(candidate, name):
			raise Invalid(
				"%r does not define %r" % (candidate, name),
				candidate, name, iface)
		candidate_method = getattr(candidate, name)
		if not callable(candidate_method):
			raise Invalid(
				"%r is not callable" % (candidate_method,),
				candidate, name, iface)
		if vtype is not None:
			if not isinstance(candidate_method, vtype):
				raise Invalid(
					"%r is not a %s" % (candidate_method, vtype),
					candidate, name, iface)
		if not method.is_valid(candidate_method):
			raise Invalid(
				"%r does not have the correct signature" % (candidate_method,),
				candidate, name, iface)
	for name in iface.names():
		if name == '__init__':
			continue
		if not hasattr(candidate, name):
			raise Invalid(
				"%r does not define %r" % (candidate, name),
				candidate, name, iface)
		candidate_attr = getattr(candidate, name)
		if not isinstance(candidate_attr, _Attribute):
			raise Invalid(
				"%r is not an attribute" % (candidate_attr,),
				candidate, name, iface)
		if not candidate_attr.is_valid(candidate):
			raise Invalid(