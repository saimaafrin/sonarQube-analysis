def process_text_links(text):
# Add rel="nofollow" to all external links
	text = re.sub(r'<a\s+(?=[^>]*href=["\'])([^>]*?)>(.*?)</a>', lambda m: f'<a {m.group(1)} rel="nofollow">{m.group(2)}</a>', text)
	
	# Linkify textual links (e.g., www.example.com or example.com)
	text = re.sub(r'(\bwww\.[^\s]+\b|\b[^\s]+\.[^\s]+\b)', lambda m: f'<a href="{m.group(0)}">{m.group(0)}</a>', text)
	
	return text