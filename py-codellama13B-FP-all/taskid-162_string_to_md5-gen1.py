from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world')
    '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib

    # md5 is a hash function that takes a string and returns its md5 hash
    # as a new string
    md5_hash = hashlib.md5(text.encode())

    # return the md5 hash of the string as a hexadecimal string
    return md5_hash.hexdigest()
