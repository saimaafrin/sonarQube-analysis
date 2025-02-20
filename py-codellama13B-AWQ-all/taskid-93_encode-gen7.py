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

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encoded_message = ""

    for char in message:
        if char.isupper():
            # Swap case for the uppercase letter
            new_char = alphabet[(alphabet.index(char) + 2) % 26]
        else:
            new_char = char.upper()

        encoded_message += new_char

    return encoded_message
