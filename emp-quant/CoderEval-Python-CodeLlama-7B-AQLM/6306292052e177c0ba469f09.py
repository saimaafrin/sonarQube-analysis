def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	if request.json:
		if 'events' in request.json:
			return True
		else:
			return False
	elif request.form:
		if request.form.get('tag') == Magic_ENV_TAG:
			return True
		else:
			return False
	else:
		return False