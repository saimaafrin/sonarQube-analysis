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

    result = []
    vowels = 'aeiouAEIOU'
    for letter in message:
        if letter in vowels:
            result.append(chr((ord(letter) + 2) % 26 + ord('A')))
        elif letter.isupper():
            result.append(letter.lower())
        elif letter.islower():
            result.append(letter.upper())
        else:
            result.append(letter)
    return ''.join(result)
