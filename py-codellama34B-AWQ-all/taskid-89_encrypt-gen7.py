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

    encrypt_dict = {'a': 'c', 'b': 'd', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'j', 'g': 'k', 'h': 'm', 'i': 'o', 'j': 'q', 'k': 's', 'l': 't', 'm': 'w', 'n': 'z', 'o': 'b', 'p': 'e', 'q': 'h', 'r': 'k', 's': 'n', 't': 'p', 'u': 'r', 'v': 'x', 'w': 'a', 'x': 'i', 'y': 'l', 'z': 'u'}
    return ''.join([encrypt_dict[c] for c in s])
