def is_fill_request_seq(seq):
# Check if seq is a list
	if not isinstance(seq, list):
		return False

	# Check if all elements in seq are instances of FillRequest
	for item in seq:
		if not isinstance(item, FillRequest):
			return False

	# If all checks pass, return True
	return True