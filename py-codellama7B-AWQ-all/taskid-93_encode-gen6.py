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

    encoded_message = ''
    for char in message:
        if char.islower():
            encoded_message += char.upper()
        else:
            encoded_message += char.lower()
    for i in range(0, len(encoded_message)):
        if encoded_message[i] in 'aeiou':
            encoded_message = encoded_message[:i] + chr((ord(encoded_message[i]) + 2) % 26) + encoded_message[i+1:]
    return encoded_message
