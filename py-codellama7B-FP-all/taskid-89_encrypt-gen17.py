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
    alf = [chr(i) for i in range(97,123)]
    res = ""
    for i in range(len(s)):
        x = s[i]
        if x in alf:
            y = alf.index(x)
            y = alf[(y-2)*2]
            res += y
        else:
            res += x
    return res

    # Another solution
    # def encrypt(s):
    #     return "".join(chr((ord(c)-97+2)%26+97) for c in s.lower())
