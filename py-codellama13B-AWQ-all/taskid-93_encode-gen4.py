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
    for char in message:
        if char.isupper():
            # swap case
            result += char.lower()
        else:
            # replace vowels
            pos = ord(char) - ord('a') + 2
            if pos > ord('z') - ord('a'):
                pos -= 26
            result += chr(ord('a') + pos)
    return result
