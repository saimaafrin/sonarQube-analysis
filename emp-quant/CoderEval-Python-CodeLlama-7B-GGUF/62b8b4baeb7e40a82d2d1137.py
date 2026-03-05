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
			raise Invalid("Missing attribute %s" % name, iface, candidate)
		candidate_method = getattr(candidate, name)
		if not callable(candidate_method):
			raise Invalid("Attribute %s is not callable" % name, iface, candidate)
		if method.func_code != candidate_method.func_code:
			raise Invalid("Method %s has wrong code" % name, iface, candidate)
		if method.func_defaults != candidate_method.func_defaults:
			raise Invalid("Method %s has wrong defaults" % name, iface, candidate)
		if method.func_doc != candidate_method.func_doc:
			raise Invalid("Method %s has wrong docstring" % name, iface, candidate)
		if method.func_name != candidate_method.func_name:
			raise Invalid("Method %s has wrong name" % name, iface, candidate)
		if method.func_dict != candidate_method.func_dict:
			raise Invalid("Method %s has wrong closure" % name, iface, candidate)
		if method.func_closure != candidate_method.func_closure:
			raise Invalid("Method %s has wrong closure" % name, iface, candidate)
		if method.func_code.co_argcount != candidate_method.func_code.co_argcount:
			raise Invalid("Method %s has wrong number of arguments" % name, iface, candidate)
		if method.func_code.co_varnames != candidate_method.func_code.co_varnames:
			raise Invalid("Method %s has wrong argument names" % name, iface, candidate)
		if method.func_code.co_filename != candidate_method.func_code.co_filename