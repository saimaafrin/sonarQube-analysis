def is_fill_compute_el(obj):
# Check if 'fill' method exists in the object's class
	if hasattr(obj, 'fill'):
		# Check if 'compute' method exists in the object's class
		if hasattr(obj, 'compute'):
			return True
	return False