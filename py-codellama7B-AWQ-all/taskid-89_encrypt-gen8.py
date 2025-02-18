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
    s=s.lower()
    a=list(s)
    for i in range(len(a)):
        if a[i].isalpha():
            a[i]=chr((ord(a[i])-97+2*2)%26+97)
    return ''.join(a)
