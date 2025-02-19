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

    vowels = 'aeiou'
    result = ''
    
    for letter in message:
        if letter.isupper():
            if letter in vowels:
                result += chr(ord(letter) + 2)
            else:
                result += letter.lower()
        else:
            if letter in vowels:
                result += chr(ord(letter) + 2)
            else:
                result += letter.upper()
    return result
