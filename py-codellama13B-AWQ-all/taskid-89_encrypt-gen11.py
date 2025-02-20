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

    s = s.lower()
    cipher = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            x = ord(c)
            x = (x - ord('a') + 2*2) % 26 + ord('a')
            cipher += chr(x)
        else:
            cipher += c
    return cipher
