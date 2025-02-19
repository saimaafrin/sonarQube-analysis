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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    encoded_msg = ""
    for letter in message:
        if letter.islower():
            new_letter = alphabet[alphabet.find(letter)+2]
            if letter in vowels:
                new_letter = new_letter.upper()
        elif letter.isupper():
            new_letter = alphabet[alphabet.find(letter)+2].lower()
            if letter in vowels:
                new_letter = new_letter.upper()
        else:
            new_letter = letter
        encoded_msg += new_letter
    return encoded_msg
