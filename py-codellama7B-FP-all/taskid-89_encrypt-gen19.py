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

    # Create a string to rotate the alphabet
    rot = 'abcdefghijklmnopqrstuvwxyz'

    # Create an empty list to hold the encrypted string
    encrypted = []

    # Loop through each character in the string and append the encrypted character to the list
    for char in s:
        # Check if the character is in the rot string
        if char in rot:
            # Get the index of the character in the rot string
            index = rot.index(char)

            # Rotate the character by 2 places
            rot_index = index + 2

            # Check if the rot_index is greater than the length of the rot string
            if rot_index > 25:
                # Subtract the length of the rot string from the rot_index
                rot_index = rot_index - 26

            # Append the encrypted character to the list
            encrypted.append(rot[rot_index])

        # Check if the character is not in the rot string
        else:
            # Append the character to the list
            encrypted.append(char)

    # Return the encrypted string
    return ''.join(encrypted)
