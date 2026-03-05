import re

def process_text_links(text):
    # Regex to find URLs
    url_regex = r'(https?://[^\s]+)'
    
    # Function to replace URL with anchor tag
    def replace_url_with_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Replace URLs in text with anchor tags
    processed_text = re.sub(url_regex, replace_url_with_link, text)
    
    return processed_text