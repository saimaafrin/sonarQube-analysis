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
            chr(ord(c) + 2 * (97 <= ord(c) <= 122))
            if c in "aeiouAEIOU"
            else c
            for c in message
        ]
    )
