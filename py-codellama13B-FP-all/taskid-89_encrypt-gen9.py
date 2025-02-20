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

    # The alphabets to be used in the encryption
    alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'cdefghijklmnopqrstuvwxyzab'
    alpha3 = 'efghijklmnopqrstuvwxyzabcd'

    # An empty string to store the encrypted output
    output = ''

    # Looping over every character in the input string
    for char in s:

        # If the character is a letter
        if char.isalpha():

            # Finding the index of the character in alpha1
            index = alpha1.find(char)

            # Creating a new character based on the index
            new_char = alpha2[index]

            # If the character is uppercase
            if char.isupper():

                # Finding the index of the character in alpha1
                index = alpha1.find(char)

                # Creating a new character based on the index
                new_char = alpha3[index]

            # Appending the new character to the output
            output += new_char

        # If the character is not a letter
        else:

            # Appending the character as is to the output
            output += char

    # Returning the encrypted output
    return output
