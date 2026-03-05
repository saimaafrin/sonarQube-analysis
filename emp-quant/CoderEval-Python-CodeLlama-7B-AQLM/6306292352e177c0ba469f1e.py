def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	# Add link attributes
	text = re.sub(r'<a href="([^"]+)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', text)
	# Linkify textual links
	text = re.sub(r'https?://\S+', r'<a href="\g<0>">\g<0></a>', text)
	return text