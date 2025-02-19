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

    # 26 = alphabet
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu = 18, vwx = 21, yz = 24
    # abc = 0, def = 3, ghi = 6, jkl = 9, mno = 12, pqr = 15, stu
