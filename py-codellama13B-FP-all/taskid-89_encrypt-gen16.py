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
    encrypted = ''
    for c in s:
        if c not in alphabet:
            encrypted += c
        else:
            index = alphabet.find(c)
            new_index = index + 2
            encrypted += alphabet[new_index]
    return encrypted
