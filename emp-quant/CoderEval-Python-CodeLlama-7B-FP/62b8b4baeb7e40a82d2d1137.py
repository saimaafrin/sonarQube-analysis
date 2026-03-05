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
		iface.providedBy(candidate)
	for name, method in iface.namesAndDescriptors():
		if name.startswith('_'):
			continue
		if not hasattr(candidate, name):
			raise Invalid("Missing attribute %r" % (name,))
		candidate_method = getattr(candidate, name)
		if not callable(candidate_method):
			raise Invalid("Attribute %r is not callable" % (name,))
		if method.im_func is not getattr(candidate_method, 'im_func'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_code is not getattr(candidate_method, 'func_code'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_defaults != getattr(candidate_method, 'func_defaults'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_doc != getattr(candidate_method, 'func_doc'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_name != getattr(candidate_method, 'func_name'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_dict != getattr(candidate_method, 'func_dict'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_globals != getattr(candidate_method, 'func_globals'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_closure != getattr(candidate_method, 'func_closure'):
			raise Invalid("Attribute %r is not the same method" % (name,))
		if method.func_code.co