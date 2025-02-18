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

    message = message.lower()
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    encoded = ''

    for i in range(len(message)):
        if message[i] in english_alphabet:
            if message[i] in vowels:
                index = english_alphabet.index(message[i]) + 2
                encoded += english_alphabet[index]
            else:
                encoded += message[i].upper()
        else:
            encoded += message[i]

    return encoded
