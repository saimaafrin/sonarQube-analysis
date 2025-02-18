def encode(message: str) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    # Build a lookup table for the vowels
    vowel_lookup = {
        'a': 'c',
        'e': 'g',
        'i': 'j',
        'o': 'm',
        'u': 'v'
    }

    # Iterate over each character in the message
    encoded_message = ''
    for char in message:

        # If the character is uppercase, switch it to lowercase
        if char.isupper():
            char = char.lower()

        # If the character is a vowel, replace it
        if char in vowel_lookup:
            char = vowel_lookup[char]

        # Add the character to the encoded message
        encoded_message += char

    return encoded_message
