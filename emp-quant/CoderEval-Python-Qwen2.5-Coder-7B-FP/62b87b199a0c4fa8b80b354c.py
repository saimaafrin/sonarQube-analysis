def _get_seq_with_type(seq, bufsize=None):
# If seq is already a sequence, return it and its type
	if isinstance(seq, (list, tuple)):
		return seq, type(seq)
	
	# If seq is not a sequence, convert it to a list
	if bufsize is None:
		bufsize = 1024
	
	seq_list = []
	for item in iter(seq, None):
		seq_list.append(item)
		if len(seq_list) >= bufsize:
			break
	
	return seq_list, list