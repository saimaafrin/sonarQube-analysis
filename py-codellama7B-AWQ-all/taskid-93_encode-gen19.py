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

    # Replace vowels with the letter 2 places ahead of it
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = []
    for i in range(len(message)):
        if message[i].lower() in vowels:
            new_message.append(chr(ord(message[i].lower()) + 2))
        else:
            new_message.append(message[i].lower())
    # Replace all other letters with their capital counterpart
    new_message_2 = []
    for i in range(len(new_message)):
        if new_message[i].islower():
            new_message_2.append(new_message[i].upper())
        else:
            new_message_2.append(new_message[i])
    return ''.join(new_message_2)
