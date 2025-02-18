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

    # +++your code here+++
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Define a new list that will hold the encrypted alphabet
    encrypted_alphabet = []
    # Loop through the alphabet and apply the encryption to each letter
    for letter in alphabet:
        # Find the index of each letter in the alphabet
        index = alphabet.index(letter)
        # Apply the encryption to each letter by rotating it down
        # by two places in the alphabet
        new_index = index + 2
        # If the new index is greater than the length of the alphabet,
        # then the letter should be encrypted to the beginning of the alphabet
        # minus the difference of the new index and the length of the alphabet
        if new_index > 25:
            encrypted_alphabet.append(alphabet[new_index - 26])
        # Otherwise, the letter should be encrypted to the new index
        else:
            encrypted_alphabet.append(alphabet[new_index])
    # Define a dictionary that maps each letter to its encrypted letter
    encrypt_dict = dict(zip(alphabet, encrypted_alphabet))
    # Define a new string that will hold the encrypted message
    encrypted_message = ''
    # Loop through each letter of the message
    for letter in s:
        # If the letter is a letter of the alphabet, then encrypt it
        if letter in alphabet:
            encrypted_message += encrypt_dict[letter]
        # Otherwise, keep the punctuation and whitespace the same
        else:
            encrypted_message += letter
    # Return the encrypted message
    return encrypted_message
