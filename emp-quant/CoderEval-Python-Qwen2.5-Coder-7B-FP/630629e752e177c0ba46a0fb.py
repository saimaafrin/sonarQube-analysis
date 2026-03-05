def send_document(url, data, timeout=10, method="post", *args, **kwargs):
# Create a session object
	session = requests.Session()

	# Set the headers for the request
	headers = {
		"Content-Type": "application/json",
	}

	# Send the request using the specified method and parameters
	response = session.request(method, url, json=data, headers=headers, timeout=timeout, *args, **kwargs)

	# Check if the response status code is 200 (OK)
	if response.status_code == 200:
		return response.json()  # Return the JSON response content
	else:
		return None  # Return None if the request was not successful