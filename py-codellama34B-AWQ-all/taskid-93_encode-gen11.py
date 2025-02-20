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
    new_message = ''
    for letter in message:
        if letter.lower() in vowels:
            idx = vowels.index(letter.lower())
            new_letter = (idx + 2) % 5
            new_message += vowels[new_letter].upper() if letter.isupper() else vowels[new_letter].lower()
        elif letter.isupper():
            new_message += letter.lower()
        else:
            new_message += letter.upper()
    return new_message
