def get_pattern(pattern, strip=True):
# If it's already a pattern, return it as is
	if isinstance(pattern, re.Pattern):
		return pattern

	# Strip spaces if required
	if strip:
		pattern = pattern.strip()

	# Return the compiled pattern
	return re.compile(pattern)