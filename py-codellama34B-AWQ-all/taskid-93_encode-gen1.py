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
    vowels_encode = 'fgpqy'
    output = ''

    for letter in message:
        if letter.isalpha():
            if letter.islower():
                output += letter.upper()
            else:
                output += letter.lower()
        else:
            output += letter

        if letter.lower() in vowels:
            letter_idx = vowels.index(letter.lower())
            output += vowels_encode[letter_idx]

    return output
