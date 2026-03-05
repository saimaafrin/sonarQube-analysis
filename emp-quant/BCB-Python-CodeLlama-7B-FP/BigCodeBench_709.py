import base64
import re
from html import unescape
import textwrap
def task_func(raw_string, line_length):
    """
    Decode a raw string from base64, decouple HTML entities, replace multiple spaces with a single space, strip leading and subsequent spaces, and wrap text to a certain line length.
    """
    # Decode the base64 string
    decoded_string = base64.b64decode(raw_string).decode("utf-8")

    # Unescape HTML entities
    unescaped_string = unescape(decoded_string)

    # Replace multiple spaces with a single space
    cleaned_string = re.sub(r"\s+", " ", unescaped_string)

    # Strip leading and subsequent spaces
    stripped_string = cleaned_string.strip()

    # Wrap text to a certain line length
    wrapped_text = textwrap.fill(stripped_string, line_length)

    return wrapped_text
raw_string = "aGVsbG8gd29ybGQ="
line_length = 20