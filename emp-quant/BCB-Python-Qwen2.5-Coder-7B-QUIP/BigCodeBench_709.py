
import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):
    # Decode the base64 encoded string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_string = decoded_bytes.decode('utf-8')
    
    # Unescape HTML entities
    unescaped_string = unescape(decoded_string, html4=True)
    
    # Replace multiple spaces with a single space
    single_spaced_string = re.sub(r'\s+', ' ', unescaped_string)
    
    # Strip leading and trailing spaces
    stripped_string = single_spaced_string.strip()
    
    # Wrap the text to the specified line length
    wrapped_text = textwrap.fill(stripped_string, width=line_length)
    
    return wrapped_text