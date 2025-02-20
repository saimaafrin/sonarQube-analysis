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

    new_message = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in message:
        if char in vowels:
            new_message += char.upper()
        elif char.isupper():
            new_message += char.lower()
        else:
            new_message += char
    return new_message
