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

    letters = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'cdefghijklmnopqrstuvwxyzab'
    result = ''
    for letter in s:
        if letter in letters:
            result += cipher[letters.index(letter)]
        else:
            result += letter
    return result
