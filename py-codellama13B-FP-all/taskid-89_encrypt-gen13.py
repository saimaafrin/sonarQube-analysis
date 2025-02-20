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

    alph = 'abcdefghijklmnopqrstuvwxyz'
    enc_alph = ''
    for i in range(len(alph)):
        enc_alph += alph[(i*2)%26]
    dec = ''
    for i in s:
        if i in alph:
            dec += enc_alph[alph.index(i)]
        else:
            dec += i
    return dec
