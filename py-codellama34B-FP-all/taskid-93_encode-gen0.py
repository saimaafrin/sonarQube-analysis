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

    # Your code here
    vowels = set("aeiouAEIOU")
    encoded = ""
    for char in message:
        if char in vowels:
            char = chr((ord(char) + 2 - 65) % 26 + 65)
        encoded += char.swapcase()
    return encoded
