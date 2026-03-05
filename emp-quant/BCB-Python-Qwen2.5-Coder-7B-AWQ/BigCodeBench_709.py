import base64
import re
from html import unescape
import textwrap
def task_func(raw_string, line_length):
    # Decode the raw string from base64
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    
    # Decouple HTML entities
    decoded_string = unescape(decoded_string)
    
    # Replace multiple spaces with a single space
    decoded_string = re.sub(r'\s+', ' ', decoded_string)
    
    # Strip leading and trailing spaces
    decoded_string = decoded_string.strip()
    
    # Wrap text to a certain line length
    wrapped_text = textwrap.fill(decoded_string, width=line_length)
    
    return wrapped_text