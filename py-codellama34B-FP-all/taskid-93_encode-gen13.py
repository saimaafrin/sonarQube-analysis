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
    enc = ''
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                enc += letter.upper()
            else:
                enc += letter.lower()
        else:
            enc += letter

    for i in range(len(enc)):
        if enc[i].lower() in vowels:
            enc = enc[:i] + chr(ord(enc[i])+2) + enc[i+1:]

    return enc
