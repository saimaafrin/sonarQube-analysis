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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = ['a', 'e', 'i', 'o', 'u']
    message_list = list(message)
    encoded = ''
    for i, character in enumerate(message):
        if character.isalpha():
            if character.islower():
                encoded += alphabet[alphabet.index(character) + 1].upper()
            else:
                encoded += alphabet[alphabet.index(character) + 1]
        else:
            encoded += character
    return encoded
