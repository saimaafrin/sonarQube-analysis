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

    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                # Shift down by two places
                result += chr((ord(char) - 65 + 2) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 2) % 26 + 97)
        else:
            result += char
    return result
