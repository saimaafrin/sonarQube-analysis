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

    # initialize empty string to hold the encrypted message
    result = ""

    # iterate over each character in the string
    for char in s:
        # check if the character is a letter
        if char.isalpha():
            # check if the character is uppercase
            if char.isupper():
                # add the encrypted character to the result
                result += chr((ord(char) + 2 - 65) % 26 + 65)
            else:
                # add the encrypted character to the result
                result += chr((ord(char) + 2 - 97) % 26 + 97)
        else:
            # add the character to the result
            result += char

    # return the result
    return result
