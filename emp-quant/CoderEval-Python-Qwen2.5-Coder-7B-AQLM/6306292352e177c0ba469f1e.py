import re

def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    # Regular expression to find URLs
    url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Function to replace URLs with linkified versions
    def replace_url(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    # Replace URLs in the text
    processed_text = url_regex.sub(replace_url, text)

    return processed_text