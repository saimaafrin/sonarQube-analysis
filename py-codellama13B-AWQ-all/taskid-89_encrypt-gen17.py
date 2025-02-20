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

    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #      The testing code is already written for you (above).
    #
    # IMPORTANT: 3. You must use a   ROTATION  approach, as described
    #    in the docstring above.  That is:
    #    -- Use the ROTATION approach to create new_alphabet.
    #    -- Use the ROTATION approach to figure out what to
    #         put in the "for" expression below.
    # IMPORTANT: 4.
    #    The function does not return anything,
    #    because the return statement has been deleted.
    # ------------------------------------------------------------------
    new_alphabet = 'lmopqrstuvwxyzabcdefghij'
    new_s = ''
    for char in s:
        new_s += new_alphabet[alphabet.index(char)]
    return new_s
