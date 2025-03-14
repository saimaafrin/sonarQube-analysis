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
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        if letter.isupper():
            result += letter.lower()
        else:
            result += letter.upper()

        if letter.lower() in vowels:
            result += vowels[vowels.index(letter.lower()) + 2]
        else:
            result += letter.lower()
    return result
