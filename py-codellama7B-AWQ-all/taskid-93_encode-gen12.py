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

    # Replace all vowels in the message with the letter 
    # that appears 2 places ahead of that vowel in the 
    # english alphabet
    message = message.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ""
    for char in message:
        if char in vowels:
            # Get the letter 2 places ahead of that vowel
            encoded_message += vowels[(vowels.index(char) + 2) % len(vowels)]
        else:
            # Keep the letter as is
            encoded_message += char
    
    # Swap case of all letters
    return encoded_message.swapcase()
