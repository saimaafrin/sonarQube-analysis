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

    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapping = {
        **{v: chr(((ord(v) - 97) + 5) % 26 + 97) for v in vowels},
        **{c: chr(97 + 26 - (ord(c) - 65)) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    }

    encoded = [mapping[c.lower()] if c.isalpha() else c for c in message]
    return ''.join(encoded)
