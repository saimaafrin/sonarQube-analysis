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

    message = message.lower()

    vowels = 'aeiou'
    vowels_positions = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 3,
        'u': 4
    }

    encoded = ''
    for letter in message:
        if letter in vowels:
            position = vowels_positions[letter]
            encoded += chr(96 + position)
        else:
            encoded += letter.upper()

    return encoded
