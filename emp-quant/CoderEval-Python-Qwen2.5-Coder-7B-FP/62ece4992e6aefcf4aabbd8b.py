def force_string(obj):
# check if obj is a bytes object
	if isinstance(obj, (bytes, np.bytes_)):
		return obj.decode('utf-8')
	else:
		return obj