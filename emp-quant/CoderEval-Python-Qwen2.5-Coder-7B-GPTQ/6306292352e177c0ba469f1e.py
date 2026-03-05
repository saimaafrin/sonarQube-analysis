import re

def process_text_links(text):
    # Regular expression to find URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    def replace_url(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Replace URLs with anchor tags
    processed_text = url_pattern.sub(replace_url, text)
    
    return processed_text