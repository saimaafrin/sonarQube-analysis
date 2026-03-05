def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	# Add link attributes
	text = re.sub(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', text)
	text = re.sub(r'<a\s+(?:[^>]*?\s+)?href=\'([^\']*)\'', r'<a href=\'\1\' target="_blank" rel="noopener noreferrer"', text)

	# Linkify textual links
	text = re.sub(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', text)
	text = re.sub(r'<a\s+(?:[^>]*?\s+)?href=\'([^\']*)\'', r'<a href=\'\1\' target="_blank" rel="noopener noreferrer"', text)

	return text