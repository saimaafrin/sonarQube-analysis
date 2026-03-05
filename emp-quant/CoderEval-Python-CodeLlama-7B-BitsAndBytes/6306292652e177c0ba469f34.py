def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		response = requests.head(url, headers={'User-Agent': USER_AGENT})
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		print(f'HTTPError: {e}')
	except requests.exceptions.ConnectionError as e:
		print(f'ConnectionError: {e}')
	except requests.exceptions.Timeout as e:
		print(f'Timeout: {e}')
	except requests.exceptions.RequestException as e:
		print(f'RequestException: {e}')
	else:
		return response.headers.get('Content-Type')