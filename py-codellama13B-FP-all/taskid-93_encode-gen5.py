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

    result = ''
    for c in message:
        if c.islower():
            result += chr(ord('A') + (ord(c) - ord('a')) + 2)
        elif c.isupper():
            result += chr(ord('a') + (ord(c) - ord('A')) + 2)
        else:
            result += c
    return result
