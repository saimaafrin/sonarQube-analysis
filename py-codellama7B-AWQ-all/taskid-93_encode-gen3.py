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

    message = message.lower()
    encoded = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Iterate through each letter in the message, adding the new encoded letter to the encoded string
    for i in range(len(message)):
        if message[i] in vowels:
            # Add 2 to the index of the vowel to get the next letter in the alphabet
            next_letter = vowels[vowels.index(message[i]) + 2]
            encoded += next_letter
        else:
            encoded += message[i].upper()
    return encoded
