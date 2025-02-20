def encrypt(s: str) -> str:
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """

    result = ""
    for char in s:
        char_code = ord(char)
        if char_code <= 122 and char_code >= 97:
            result += chr((char_code + 2) % 26 + 97)
        elif char_code <= 90 and char_code >= 65:
            result += chr((char_code + 2) % 26 + 65)
        else:
            result += char

    return result
