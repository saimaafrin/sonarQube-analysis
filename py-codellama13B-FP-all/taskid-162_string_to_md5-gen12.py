from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world')
    '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # You need to import the necessary library here.
    import hashlib

    # You need to complete this function.
    return hashlib.md5(text.encode('utf-8')).hexdigest() if text else None
