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

    new_message = ""
    vowels = 'aeiou'
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                new_message += letter.upper()
            elif letter.isupper():
                new_message += letter.lower()
            elif letter in vowels:
                index = vowels.index(letter)
                new_message += vowels[index-2]
            else:
                new_message += letter
        else:
            new_message += letter
    return new_message
