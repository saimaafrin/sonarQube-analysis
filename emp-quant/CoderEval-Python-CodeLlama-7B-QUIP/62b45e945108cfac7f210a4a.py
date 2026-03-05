def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0
	for root in self.roots:
		num_objects += root.validate(validate_objects, check_digests, show_warnings)
		good_objects += root.good_objects
	return num_objects, good_objects