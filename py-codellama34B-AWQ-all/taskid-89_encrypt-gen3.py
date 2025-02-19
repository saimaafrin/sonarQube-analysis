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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'nopqrstuvwxyzabcdefghijklm'
    for i in range(len(s)):
        if s[i] in alphabet:
            result += alphabet2[alphabet.index(s[i])]
        else:
            result += s[i]
    return result
