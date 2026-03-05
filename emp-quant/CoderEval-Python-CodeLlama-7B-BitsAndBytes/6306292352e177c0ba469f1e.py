def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	# Add attributes to links
	text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
	# Linkify textual links
	text = re.sub(r'\b(https?://[^\s]+)\b', r'<a href="\1" target="_blank">\1</a>', text)
	return text