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
    encoded = ''
    for char in message:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        if char in vowels:
            index = vowels.index(char)
            new_index = (index + 2) % 5
            char = vowels[new_index]
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
        encoded += char
    return encoded
