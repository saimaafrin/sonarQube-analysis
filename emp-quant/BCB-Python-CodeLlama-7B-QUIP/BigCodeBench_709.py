
import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):
    # Decode the base64 string
    decoded_string = base64.b64decode(raw_string).decode("utf-8")

    # Unescape any HTML entities
    unescaped_string = unescape(decoded_string)

    # Replace multiple spaces with a single space
    cleaned_string = re.sub(" +", " ", unescaped_string)

    # Strip leading and subsequent spaces
    trimmed_string = cleaned_string.strip()

    # Wrap the text to the specified line length
    wrapped_text = textwrap.wrap(trimmed_string, line_length)

    return wrapped_text