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

    # Your code here
    alph = 'abcdefghijklmnopqrstuvwxyz'
    enc = ''
    for char in s:
        if char.isalpha():
            pos = alph.index(char) + 4
            if pos > 25:
                pos -= 26
            enc += alph[pos]
        else:
            enc += char
    return enc
