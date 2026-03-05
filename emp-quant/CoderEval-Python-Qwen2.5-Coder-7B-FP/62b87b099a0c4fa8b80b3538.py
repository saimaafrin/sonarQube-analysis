def is_fill_request_el(obj):
# Check if 'fill' attribute exists
	if not hasattr(obj, 'fill'):
		return False

	# Check if 'request' attribute exists
	if not hasattr(obj, 'request'):
		return False

	return True