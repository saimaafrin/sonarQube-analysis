def dict_insert(dic, val, key, *keys):
# if there are no more keys left to process, then we have reached the
	# last key and can set its value
	if not keys:
		dic[key] = val
	else:
		# check if the current key exists in the dictionary. If it does not,
		# create an empty dictionary for it.
		if key not in dic:
			dic[key] = {}
		# recursively call this function with the next key in the chain
		dict_insert(dic[key], val, *keys)