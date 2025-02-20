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
    encoded_message = ''
    for char in message:
        # vowels = ['a', 'e', 'i', 'o', 'u']
        if char in ['a', 'e', 'i', 'o', 'u']:
            char = get_next_vowel(char)
        elif char in ['A', 'E', 'I', 'O', 'U']:
            char = get_previous_vowel(char)
        else:
            pass
        encoded_message += char
    return encoded_message
