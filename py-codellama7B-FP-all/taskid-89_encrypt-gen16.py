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
    s = list(s)
    for i in range(len(s)):
        for j in range(len(alphabet)):
            if s[i] == alphabet[j]:
                s[i] = alphabet[j + 2]
    return ''.join(s)
