def strip_root(path, root):
# Check if the path starts with the root
	if not path.startswith(root):
		# Raise an error if it doesn't
		raise ValueError(f"Path '{path}' does not start with root '{root}'")

	# Strip the root from the path
	return path[len(root):]  # Return the part of the path after the root