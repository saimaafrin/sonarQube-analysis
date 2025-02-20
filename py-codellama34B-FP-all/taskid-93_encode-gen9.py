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

    for letter in message:
        if letter.islower():
            if letter in vowels:
                # Convert letter to upper case
                encoded += letter.upper()
                # Shift letter
                encoded += chr(ord(letter) + 2)
            else:
                # Convert letter to upper case
                encoded += letter.upper()
        else:
            if letter in vowels:
                # Shift letter
                encoded += chr(ord(letter) + 2)
                # Convert letter to lower case
                encoded += letter.lower()
            else:
                # Convert letter to lower case
                encoded += letter.lower()
    return encoded
