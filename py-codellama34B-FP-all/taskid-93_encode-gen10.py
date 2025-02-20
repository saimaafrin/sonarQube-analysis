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
    for char in message:
        result += char.upper() if char.islower() else char.lower()

    for i in range(len(result)):
        if result[i] in vowels:
            result = result[:i] + chr(ord(result[i]) + 2) + result[i + 1:]

    return result
