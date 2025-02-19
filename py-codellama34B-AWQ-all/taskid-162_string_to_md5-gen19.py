from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world')
    '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    import re

    if not isinstance(text, str):
        return None

    if len(text) == 0:
        return None

    text_to_hash = re.sub(r'\s+', '', text)
    return hashlib.md5(text_to_hash.encode('utf-8')).hexdigest()
