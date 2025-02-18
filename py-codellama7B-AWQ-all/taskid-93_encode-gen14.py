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

    encoded = ''
    for c in message:
        if c.islower():
            if c in 'aeiou':
                encoded += chr((ord(c) + 2) % 26)
            else:
                encoded += c.upper()
        else:
            if c in 'AEIOU':
                encoded += chr((ord(c) - 2) % 26)
            else:
                encoded += c.lower()
    return encoded
