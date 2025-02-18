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
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for letter in message:
        if letter.islower():
            letter = letter.upper()
        elif letter.isupper():
            letter = letter.lower()
        if letter in vowels:
            index = vowels.index(letter) + 2
            letter = english_alphabet[index]
        encoded += letter
    return encoded
