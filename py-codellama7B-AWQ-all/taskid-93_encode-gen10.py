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

    # 1. Make the message all lowercase
    message = message.lower()
    
    # 2. Replace all vowels with the letter that comes 2 places ahead
    message = message.replace('a', 'c')
    message = message.replace('e', 'g')
    message = message.replace('i', 'k')
    message = message.replace('o', 'm')
    message = message.replace('u', 's')
    message = message.replace('y', 'b')
    message = message.replace('c', 'a')
    message = message.replace('g', 'e')
    message = message.replace('k', 'i')
    message = message.replace('m', 'o')
    message = message.replace('s', 'u')
    message = message.replace('b', 'y')
    
    # 3. Uppercase all letters
    message = message.upper()
    
    return message
