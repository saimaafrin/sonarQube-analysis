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

    return "".join(
        [
            chr((ord(i.upper()) - 65) % 32 + 65)
            if i.isalpha()
            else i.upper()
            if i in ["A", "E", "I", "O", "U", "Y"]
            else i
            if i in ["a", "e", "i", "o", "u", "y"]
            else chr((ord(i) - 65) % 32 + 65)
            if i.isalpha()
            else i
        ]
        for i in message
    )
