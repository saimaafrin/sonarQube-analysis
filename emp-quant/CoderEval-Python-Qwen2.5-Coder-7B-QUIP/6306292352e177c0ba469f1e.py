import re
from urllib.parse import urlparse

def process_text_links(text):
    # Regular expression to find URLs in the text
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    def replace_url(match):
        # Extract the URL from the match
        url = match.group(0)
        # Check if the URL is valid
        if urlparse(url).scheme:
            # Add attributes to the URL
            return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
        return url

    # Replace URLs in the text with linkified versions
    processed_text = re.sub(url_pattern, replace_url, text)
    return processed_text