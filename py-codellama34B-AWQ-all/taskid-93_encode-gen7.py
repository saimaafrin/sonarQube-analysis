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
    encoded_msg = ''
    for letter in message:
        if letter.islower():
            encoded_msg += letter.upper()
        elif letter.isupper():
            encoded_msg += letter.lower()
        else:
            encoded_msg += letter
    
    for i in range(len(encoded_msg)):
        letter = encoded_msg[i]
        if letter in vowels:
            new_letter = chr((ord(letter)+2-ord('a'))%26+ord('a'))
            encoded_msg = encoded_msg[:i] + new_letter + encoded_msg[i+1:]
    return encoded_msg
