def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	if request.headers.get('Content-Type') == 'application/json':
		try:
			request_body = request.get_json()
			if 'events' in request_body:
				return True
			else:
				return False
		except ValueError:
			return False
	elif request.headers.get('Content-Type') == 'application/xml':
		try:
			request_body = request.get_data()
			if request_body.decode('utf-8').find(Magic_ENV_TAG) != -1:
				return True
			else:
				return False
		except ValueError:
			return False
	else:
		return False