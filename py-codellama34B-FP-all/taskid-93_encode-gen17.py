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
    vowels = 'aeiou'
    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        elif char in vowels:
            result += chr(ord(char) + 2)
        else:
            result += char
    return result
