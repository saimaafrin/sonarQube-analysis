
import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):
    # Decode the base64 encoded string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_str = decoded_bytes.decode('utf-8')
    
    # Decouple HTML entities
    decoded_str = unescape(decoded_str)
    
    # Replace multiple spaces with a single space
    decoded_str = re.sub(r'\s+', ' ', decoded_str)
    
    # Strip leading and trailing spaces
    decoded_str = decoded_str.strip()
    
    # Wrap text to the specified line length
    wrapped_text = textwrap.fill(decoded_str, width=line_length)
    
    return wrapped_text