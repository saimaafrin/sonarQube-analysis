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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_str = ''
    for c in s:
        if c.isalpha():
            i = alphabet.index(c)
            encrypt_str += alphabet[(i + 2 * 2) % 26]
        else:
            encrypt_str += c

    return encrypt_str
