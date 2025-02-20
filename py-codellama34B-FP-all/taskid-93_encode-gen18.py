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

    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = []
    for char in message:
        if char.islower():
            if char in vowels:
                encoded.append(chr(ord('a') + (ord(char) + 2 - ord('a')) % 26))
            else:
                encoded.append(char.upper())
        elif char.isupper():
            if char in [vowel.upper() for vowel in vowels]:
                encoded.append(chr(ord('A') + (ord(char) + 2 - ord('A')) % 26))
            else:
                encoded.append(char.lower())
        else:
            raise ValueError('Invalid character.')
    return ''.join(encoded)
