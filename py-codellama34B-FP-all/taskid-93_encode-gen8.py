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

    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.islower():
            encoded_message += char.upper()
        elif char.isupper():
            encoded_message += char.lower()
        elif char in vowels:
            encoded_message += chr(ord(char) + 2)
        else:
            encoded_message += char
    return encoded_message
