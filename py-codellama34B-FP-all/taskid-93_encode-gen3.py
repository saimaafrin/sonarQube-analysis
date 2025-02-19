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


    # Replace all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet
    vowels = 'aeiou'
    enc_vowels = 'gjmpqy'
    translator = str.maketrans(vowels, enc_vowels)
    message = message.translate(translator)

    # Swap case of all letters
    message = message.swapcase()

    return message
