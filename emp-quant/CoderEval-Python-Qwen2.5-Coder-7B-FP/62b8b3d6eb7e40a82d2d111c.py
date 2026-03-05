def _normalizeargs(sequence, output=None):
# TODO: This function is not used anywhere. Remove it?
	if output is None:
		output = []

	for arg in sequence:
		if isinstance(arg, Declaration):
			output.append(arg)
		elif isinstance(arg, tuple):
			_normalizeargs(arg, output=output)
		else:
			output.append(arg)

	return output