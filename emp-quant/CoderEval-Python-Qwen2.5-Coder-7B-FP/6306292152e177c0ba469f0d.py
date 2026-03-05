def identify_request(request: RequestType) -> bool:
# Check if the request body is a dictionary and contains an 'events' key
	if isinstance(request.body, dict) and 'events' in request.body:
		return True
	else:
		return False