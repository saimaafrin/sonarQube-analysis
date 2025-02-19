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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = ""
    for letter in s:
        num = alphabet.find(letter)
        if num == -1:
            encrypt = encrypt + letter
        else:
            num += 2 * 2
            if num >= 26:
                num -= 26
            encrypt = encrypt + alphabet[num]
    return encrypt
