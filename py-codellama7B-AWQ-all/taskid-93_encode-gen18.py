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


    # Initialize a dictionary to store the vowels in english alphabet.
    vowels = {
        'a': 'A',
        'e': 'E',
        'i': 'I',
        'o': 'O',
        'u': 'U',
    }

    # Initialize a string to store the encoded message.
    encoded_message = ''

    # Iterate through the message and replace each vowel.
    for char in message:
        if char in vowels:
            # Replace the current char with the one that is 2 places ahead.
            encoded_message += vowels[char]
        else:
            # Replace the current char with the same char.
            encoded_message += char

    # Return the encoded message.
    return encoded_message
