def set_cut_chars(self, before: bytes, after: bytes) -> None:
# Validate input
	if not isinstance(before, bytes):
		raise ValueError("before must be a bytes object")
	if not isinstance(after, bytes):
		raise ValueError("after must be a bytes object")

	# Set the delimiters
	self._cut_before = before
	self._cut_after = after

	# Reset the split state
	self.reset_split_state()