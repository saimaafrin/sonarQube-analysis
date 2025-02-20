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
    x = ""
    for i in s:
        if i in "abcdefghijklmnopqrstuvwxyz":
            i = ord(i)
            i -= 97
            i = (i * 2) % 26
            i += 97
            i = chr(i)
        x += i
    return x
