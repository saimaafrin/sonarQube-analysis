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

    # The message, all letters are lowercase. 
    # So all vowels will be in the 0 to 4 indexes. 
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = ''
    for i, letter in enumerate(message):
        if letter.isalpha():
            # Replace the vowels with the next letter. 
            if letter.lower() in vowels:
                new_message += vowels[vowels.index(letter.lower()) + 2]
            else:
                new_message += letter.swapcase()
        else:
            new_message += letter
    return new_message
