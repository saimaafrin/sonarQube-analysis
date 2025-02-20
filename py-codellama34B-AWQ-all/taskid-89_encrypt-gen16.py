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

    cipher = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                if ord(char) + 2 > ord('Z'):
                    cipher += chr(ord(char) - 24)
                else:
                    cipher += chr(ord(char) + 2)
            else:
                if ord(char) + 2 > ord('z'):
                    cipher += chr(ord(char) - 24)
                else:
                    cipher += chr(ord(char) + 2)
        else:
            cipher += char
    return cipher
