def parse_diaspora_webfinger(document: str) -> Dict:
# Parse the JSON document
	data = json.loads(document)
	
	# Extract the hcard_url from the webfinger
	hcard_url = data['links'][0]['href']
	
	# Return a dictionary with the hcard_url
	return {'hcard_url': hcard_url}
```

This function takes a string `document` as input and returns a dictionary containing the `hcard_url`. The function first parses the JSON document using `json.loads()`, then extracts the `hcard_url` from the `links` array. Finally, it returns a dictionary with the extracted `hcard_url`.