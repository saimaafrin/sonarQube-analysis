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

    # Initialize encrypted string to return
    encrypted = ""

    # Loop through each character in string s
    for char in s:

        # If character is a letter...
        if char.isalpha():

            # ...shift character by rotating alphabet two places
            if char.islower():
                encrypted += chr((ord(char) - 97 + 2) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + 2) % 26 + 65)

        # If character is not a letter...
        else:

            # ...add character to encrypted string
            encrypted += char

    # Return encrypted string
    return encrypted
