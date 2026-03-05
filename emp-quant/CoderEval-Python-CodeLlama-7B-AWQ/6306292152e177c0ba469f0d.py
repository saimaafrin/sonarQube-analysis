def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if request.json is None:
		return False
	if "events" not in request.json:
		return False
	return True