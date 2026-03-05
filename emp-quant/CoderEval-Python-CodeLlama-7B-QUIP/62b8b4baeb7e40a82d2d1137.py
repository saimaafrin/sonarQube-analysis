def verifyObject(iface, candidate, tentative=False):
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
		iface = iface.__providedBy__
		if iface is None:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if iface.providedBy(candidate) is False:
			raise Invalid(
				"candidate does not provide the interface", candidate)
	for name in dir(iface):
		if name.startswith('__'):
			continue
		attr = getattr(iface, name)
		if not hasattr(candidate, name):
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr is None:
			continue
		if attr.__doc__ is None:
			continue
		if attr.__doc__ != getattr(candidate, name).__doc__:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr.__doc__ is not None:
			continue
		if attr.__name__ != getattr(candidate, name).__name__:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr.__name__ is not None:
			continue
		if attr.__code__ is not getattr(candidate, name).__code__:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr.__code__ is not None:
			continue
		if attr.__closure__ is not getattr(candidate, name).__closure__:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr.__closure__ is not None:
			continue
		if attr.__annotations__ is not getattr(candidate, name).__annotations__:
			raise Invalid(
				"candidate does not provide the interface", candidate)
		if attr.__annotations__ is