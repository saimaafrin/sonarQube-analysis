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
    result = ''
    for i in range(len(s)):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz':
            if s[i] == 'z':
                result += 'a'
            else:
                result += chr((ord(s[i]) + 2 * 2) % 26 + ord('a'))
        else:
            result += s[i]
    return result
