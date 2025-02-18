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

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    translated = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].islower():
                translated += alphabets[alphabets.index(message[i]) + 2]
            else:
                translated += alphabets[alphabets.index(message[i]) - 2].upper()
        else:
            translated += message[i]
    return translated
