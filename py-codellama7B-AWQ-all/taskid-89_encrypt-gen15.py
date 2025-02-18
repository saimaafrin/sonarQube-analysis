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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in range(len(s)):
        index = alphabet.find(s[i])
        new_index = (index + 2 * 2) % 26
        result += alphabet[new_index]
    return result
