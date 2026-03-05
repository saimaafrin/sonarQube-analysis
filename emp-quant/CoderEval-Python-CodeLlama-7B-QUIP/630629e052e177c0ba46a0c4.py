def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	import json
	import re
	
	# Parse the document
	document = json.loads(document)
	
	# Get the value of hcard_url
	hcard_url = document["links"][0]["href"]
	
	# Get the value of hcard_url
	hcard_url = re.sub(r"^https://([a-z0-9\-]+).diaspora.net/", r"https://\1.diaspora.net/", hcard_url)
	
	# Return the value of hcard_url
	return hcard_url