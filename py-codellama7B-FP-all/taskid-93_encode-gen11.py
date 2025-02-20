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
    new_message = ''
    for i, c in enumerate(message):
        if c.isalpha():
            if c.isupper():
                new_message += chr((ord(c) - 65 + 2) % 26 + 65)
            else:
                new_message += chr((ord(c) - 97 + 2) % 26 + 97)
        else:
            new_message += c
    return new_message
