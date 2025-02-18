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

    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ''
    for i, c in enumerate(message):
        if c.islower():
            if c in english_alphabet:
                new_message += english_alphabet[english_alphabet.index(c) + 2]
            else:
                new_message += c
        else:
            if c in english_alphabet:
                new_message += english_alphabet[english_alphabet.index(c) - 2]
            else:
                new_message += c
    return new_message
