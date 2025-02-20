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

    message_list = list(message)
    
    # Swap case of all letters
    for i in range(len(message_list)):
        if message_list[i].islower():
            message_list[i] = message_list[i].upper()
        else:
            message_list[i] = message_list[i].lower()
    
    # Replace all vowels with the letter 2 places ahead in the alphabet
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(message_list)):
        if message_list[i].lower() in vowels:
            index = vowels.index(message_list[i].lower())
            message_list[i] = chr(ord(message_list[i]) + 2)

    return ''.join(message_list)
