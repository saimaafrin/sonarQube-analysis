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

    res = []
    for ch in s:
        if ch.isalpha():
            res.append(chr((ord(ch) - ord('a') + 2) % 26 + ord('a')))
        else:
            res.append(ch)
    return ''.join(res)
